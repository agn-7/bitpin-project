from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)

from .serializers import ContentSerializer
from .models import Content
from star_ratings.models import UserRating, Rating


class ContentView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)
    http_method_names = ("get", "head")
    renderer_classes = (JSONRenderer,)
    serializer_class = ContentSerializer

    def get_queryset(self, user):
        # return Content.objects.all()  # worst one
        # return Content.objects.select_related("rating").all()  # 10% more performance
        # return Content.objects.select_related("rating").prefetch_related("rating__user_ratings")
        return Content.objects.select_related("rating").prefetch_related("rating__user_ratings").prefetch_related("rating__user_ratings__user")  # 20% more performance
        r3 = Content.objects.select_related("rating").prefetch_related("rating__user_ratings")
        selected_users = UserRating.objects.select_related("user_set").filter(rating__user_ratings__user__id=1)
        return r3.prefetch_related(Prefetch("rating", queryset=selected_users))
        reverse_related = Content.objects.select_related("rating")
        reverse_prefetch = Rating.objects.prefetch_related("user_ratings")
        return reverse_related.prefetch_related(
            Prefetch("rating", queryset=reverse_prefetch)
        ).all()  # the same with select_related

    def get(self, request, format=None):
        try:
            content_list = self.get_queryset(request.user.id)
            if content_list:
                serializer = ContentSerializer(
                    content_list, many=True, context={"user_id": request.user.id}
                )
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

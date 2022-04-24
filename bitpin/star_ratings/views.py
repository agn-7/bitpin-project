from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication)


from .models import UserRating


class RatingView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)
    http_method_names = ('post',)
    # serializer_class = UserRatingSerializer  # TODO :: Add a serilizer to create and update the model.

    def post(self, request, *args, **kwargs):
        content_id = self.kwargs['content_id']
        score = request.POST['score']
        user_id = request.user.id

        try:
            UserRating.objects.update_or_create(
                user_id=user_id,
                rating_id=content_id,
                defaults={"score": score}
            )
            return Response('Done', status=status.HTTP_201_CREATED)
        except Exception as exc:
            return Response('Error', status=status.HTTP_400_BAD_REQUEST)

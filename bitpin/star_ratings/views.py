from __future__ import unicode_literals

from django.utils.datastructures import MultiValueDictKeyError

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
        try:
            try:
                content_id = self.kwargs['content_id'] 
            except KeyError:
                content_id = request.POST['content_id']
            score = request.POST['score']
            user_id = request.user.id

            res = UserRating.objects.update_or_create(
                user_id=user_id,
                rating_id=content_id,
                defaults={"score": score}
            )
            if res[-1]:
                '''Means created'''
                return Response('Created', status=status.HTTP_201_CREATED)
            else:
                '''Means updated'''
                return Response('Updated', status=status.HTTP_200_OK)            
        except MultiValueDictKeyError as exc:
            return Response(f"Error: {exc} is missing", status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            print(exc)
            return Response(f"Error: {exc}", status=status.HTTP_400_BAD_REQUEST)

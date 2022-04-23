from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import View
from graphene import ObjectType

from rest_framework import generics, permissions, renderers, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication)

from .serializers import ContentSerializer
from .models import Content

class ContentView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)
    http_method_names = ('get', 'head')
    renderer_classes = (JSONRenderer,)
    serializer_class = ContentSerializer

    def get_queryset(self):
        return Content.objects.all()

    def get(self, request, format=None):
        try:
            content_list = self.get_queryset()
            if content_list:
                serializer = ContentSerializer(content_list, many=True, context={'user_id': request.user.id})
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
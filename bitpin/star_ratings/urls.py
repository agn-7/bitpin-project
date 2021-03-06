from __future__ import unicode_literals

from django.urls import path

from . import views


urlpatterns = [
    path(route="<int:content_id>/", view=views.RatingView.as_view(), name="rate"),
    path(route="", view=views.RatingView.as_view(), name="rate"),
]


app_name = "star_ratings"

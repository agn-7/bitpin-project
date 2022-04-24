from django.urls import path

from . import views


urlpatterns = [
    path(route="", view=views.ContentView.as_view(), name="content_list"),
]

"""bitpin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views


openapi_info = openapi.Info(
    title="bitpin API",
    default_version='v1',
    description="API to access bitpin",
    terms_of_service="https://github.com/agn-7/bitpin",
    license=openapi.License(name="MIT License"),
)

schema_view = get_schema_view(
    openapi_info,
    public=True,
    permission_classes=()
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='api/v1/',
        view=include('contents.urls')
    ),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=86400), name='api_docs'),
]

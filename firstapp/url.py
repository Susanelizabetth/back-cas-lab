from django.contrib import admin
from django.urls import path
from django.urls.conf import include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import os
from .views import Test
app_name = "firstapp"
schema_view = get_schema_view(
    openapi.Info(
        title="Djoser API",
        default_version="v1",
        description="REST implementation of Django authentication system. djoser library provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation. It works with custom user model.",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    url=os.environ.get("SWAGGER_BASE_URL", ""),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
 path("register", register_request, name="register"),
  path('admin/', admin.site.urls),
    path(r'swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('test', Test.as_view()),
    path('api/v1/', include('djoser.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

   
]

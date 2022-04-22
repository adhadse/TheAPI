"""TheAPI URL Configuration

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
from django.urls import path, re_path, include
from rest_framework.schemas import get_schema_view as get_default_schema_view
from drf_yasg.views import get_schema_view as yasg_get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view = yasg_get_schema_view(
   openapi.Info(
      title="The API",
      default_version='1.0.0',
      description="API sering Anurag Dhadse Projects",
      terms_of_service="https://developer.anuragdhadse.com/terms/",
      contact=openapi.Contact(email="hi@anuragdhadse.com"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include(('apicore.urls', 'apicore'), namespace='apicore')),
    re_path('^deepdub/', include(('deepdub.urls', 'deepdub'), namespace='deepdub')),
    re_path('^schema(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('^schema/', get_default_schema_view(
        title="TheAPI",
        description="API sering Anurag Dhadse Projects",
        version='1.0.0',
        url='https://api.anuragdhadse.com'
    ), name='openapi-schema'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('apiauth/', include('rest_framework.urls', namespace='rest_framework'))
]

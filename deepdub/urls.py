from django.urls import path
from deepdub import views

appname = 'deepdub'
urlpatterns = [
    path('', views.deepdub_redirect, name='deepdubRedirect'),
    path('check/', views.SampleView.as_view(), name='check'),
]

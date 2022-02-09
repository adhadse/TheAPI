from django.urls import path
from deepdub import views

appname = 'deepdub'
urlpatterns = [
    path('check/', views.SampleView.as_view(), name='check'),
    path('check/', views.SampleView.as_view(), name='checkPost'),
]
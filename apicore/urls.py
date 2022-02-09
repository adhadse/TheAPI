from django.urls import path, re_path
from apicore import views

app_name = "home"
urlpatterns = [
    path('', views.redirect_view, name='redirectView'),
]

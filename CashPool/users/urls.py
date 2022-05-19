from django.urls import include, path, re_path
from rest_framework import routers

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    # path('login', views.login, name='login')
]
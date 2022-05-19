from django.urls import include, path, re_path
from rest_framework import routers

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us')
]
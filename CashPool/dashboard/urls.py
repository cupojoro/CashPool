from django.urls import include, path, re_path
from rest_framework import routers

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('plaid', views.sandbox, name="sandbox"),
    path('plaid/api', views.PlaidAPI.as_view() )
]
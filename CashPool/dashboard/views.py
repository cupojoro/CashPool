from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User

from .PlaidUtilities.PlaidManager import plaid_manager

def main(request):
    context = {"page_title": "Test Title"}
    return render(request, "dashboard/sandbox/html/main.html", context)

def red(request):
    return HttpResponseRedirect("plaid?oauth_state_id=3b5d54a0-ab58-4255-9669-dce8fa48fb04")

def sandbox(request):
    link_token = plaid_manager.generate_link_token()
    print(link_token)
    context = {"link_token": link_token}
    return render(request, "sandbox/html/sandbox.html", context)

class PlaidAPI(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        print(request)
        print(dict(request.query_params))
        return Response({"Test": "Success"})
        # return Response(data, status=None, template_name=None, headers=None, content_type=None)

    def post(self, request, format=None):
        print(request)
        print(request.data)
        return Response({"Test": "Success"})
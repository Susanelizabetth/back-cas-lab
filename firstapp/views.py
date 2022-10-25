from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.urls import re_path as url
from rest_framework_swagger.views import get_swagger_view
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

	from rest_framework.permissions import IsAuthenticated
import rest_framework.permissions


class Test(APIView):
    permission_classes = [rest_framework.permissions.AllowAny]

    def get(self, request):

        return Response({"test": "test"})


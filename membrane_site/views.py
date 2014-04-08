from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


def home(request):
	message = 'Hello World'
	return HttpResponse(message)
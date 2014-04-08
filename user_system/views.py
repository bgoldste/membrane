from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


class MyView(TemplateView):

	template_name = "user_system/home.html"

	

	def get_context_data(self, **kwargs):
		context = super(MyView, self).get_context_data(**kwargs)
		context['users'] = User.objects.all()
		context['groups'] = Group.objects.all()
		return context
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
        	return super(MyView, self).dispatch(*args, **kwargs)

class UserDetailView(generic.DetailView):

	model = User
	slug_field = 'username'

	def get_context_data(self, **kwargs):
	    context = super(UserDetailView, self).get_context_data(**kwargs)
	    return context


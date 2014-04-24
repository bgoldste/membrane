from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User, Group
from social_auth.models import UserSocialAuth
from .forms import TweetForm
from user_system.models import TweetToSend
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.generic.edit import CreateView
import tweepy

# Create your views here.


class MyView(TemplateView):

	template_name = "user_system/home.html"


	def get_context_data(self, **kwargs):
		context = super(MyView, self).get_context_data(**kwargs)
		context['users'] = User.objects.all()
		context['groups'] = Group.objects.all()
	
		context['tweets'] = TweetToSend.objects.all()
 		return context
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
        	return super(MyView, self).dispatch(*args, **kwargs)

class TweetView(CreateView):
	fields = ['original_tweet']
	model = TweetToSend
	success_url = '/send_tweet2'
	form_class = TweetForm

	def post(self, request, *args, **kwargs):
		
		form = TweetForm(request.POST)
		if form.is_valid():

			data = form.cleaned_data
  			field = data['original_tweet']

			current_user = UserSocialAuth.objects.get(user__username = request.user)
			consumer_key = settings.TWITTER_CONSUMER_KEY
			consumer_secret = settings.TWITTER_CONSUMER_SECRET
			access_token = current_user.tokens['oauth_token']
			access_token_secret = current_user.tokens['oauth_token_secret']

			auth = tweepy.OAuthHandler(consumer_key, consumer_secret)	
			auth.set_access_token(access_token, access_token_secret)

			api = tweepy.API(auth)

			# If the authentication was successful, you should
			# see the name of the account print out
		

			# If the application settings are set for "Read and Write" then
			# this line should tweet out the message to your account's 
			# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
			api.update_status(field)

			return HttpResponse("<html><body>Tweet sent!!!!</body></html>")

		else:
			
			return render(request, 'user_system/tweettosend_form.html', {
				'form' : form,
				})





	
class UserDetailView(generic.DetailView):

	model = User
	slug_field = 'username'

	def get_context_data(self, **kwargs):
	    context = super(UserDetailView, self).get_context_data(**kwargs)
	    return context

def twitter_view(request):
	current_user = UserSocialAuth.objects.get(user__username = request.user)
	consumer_key = settings.TWITTER_CONSUMER_KEY
	consumer_secret = settings.TWITTER_CONSUMER_SECRET
	access_token = current_user.tokens['oauth_token']
	access_token_secret = current_user.tokens['oauth_token_secret']

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)	
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	# If the authentication was successful, you should
	# see the name of the account print out
	print api.me().name

	# If the application settings are set for "Read and Write" then
	# this line should tweet out the message to your account's 
	# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
	api.update_status('Something new!!')

	return HttpResponse("<html><body>Tweet sent!</body></html>")

def send_tweet(request, str):	
	current_user = UserSocialAuth.objects.get(user__username = request.user)
	consumer_key = settings.TWITTER_CONSUMER_KEY
	consumer_secret = settings.TWITTER_CONSUMER_SECRET		
	access_token = current_user.tokens['oauth_token']
	access_token_secret = current_user.tokens['oauth_token_secret']

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)	
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	api.update_status(str)


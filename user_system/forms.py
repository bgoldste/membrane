from django import forms
from django.forms import ModelForm
from .models import TweetToSend
from django.core.exceptions import ValidationError
from social_auth.models import UserSocialAuth
from django.contrib.auth.models import User, Group



# move to another location after it works
#  how to deal with upper/lower case





def contains_blacklist(str):
	black_list = ('shit', 'fuck','piss', 'ass', 'anus', 'blow job', 'bitch', 'cunt', 'boner', 'negro', 'beaner',)
	if any(x in str for x in black_list):
		return 0;
	else:
		return 1;

class TweetForm(ModelForm):
	


	class Meta:
		model = TweetToSend
		widgets = {
			'original_tweet' : forms.TextInput(attrs = {'placeholder' :'write your tweet here', }),
				

		}
	def clean_original_tweet(self):
		tweet = self.cleaned_data['original_tweet']
		if (len(tweet) >= 140):
			raise ValidationError("Error tweet too long!!")

		
		if (contains_blacklist(tweet) == 0):
			raise ValidationError("Would you kiss your mother with that mouth? Try again, smarty-pants.")
		
		return tweet
		"""
	def save(self, commit = True):
		tweet = self.cleaned_data['original_tweet']
		instance = super(TweetForm, self).save(commit = commit)
		self.send_tweet(tweet)
		return instance
		"""





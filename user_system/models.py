from django.db import models
from social_auth.models import UserSocialAuth
from django.core.urlresolvers import reverse


# Create your models here.
class TweetToSend(models.Model):
	original_tweet = models.CharField(max_length = 140)
	date = models.DateTimeField(auto_now_add=True)
	fit_to_send = models.BooleanField(default=False)
	user = models.ForeignKey(UserSocialAuth)
	


	def __unicode__(self):
		return unicode(self.original_tweet)



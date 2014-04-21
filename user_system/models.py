from django.db import models


# Create your models here.
class TweetToSend(models.Model):
	original_tweet = models.CharField(max_length = 140)

	def __unicode__(self):
		return unicode(self.original_tweet)



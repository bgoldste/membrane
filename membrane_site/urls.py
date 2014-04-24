from django.conf.urls import patterns, include, url
from user_system.views import MyView, UserDetailView, twitter_view, TweetView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.http import HttpResponse
import requests
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'membrane_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social_auth.urls')),
    url(r'^register/$', CreateView.as_view(
    	template_name ='register.html',
    	form_class = UserCreationForm,
    	success_url = '/'
    	)),
    url(r'^login/$', 'django.contrib.auth.views.login' , name = 'login'),
    url(r'^$', MyView.as_view(), name='home'),
    url(r'^view1/' , MyView.as_view(), name='my-view' ),
    url(r'', include('social_auth.urls')),
    url(r'^users/(?P<slug>[-_\w]+)/$', UserDetailView.as_view(), name='article-detail'),
    url(r'^logout/$', 'django.contrib.auth.views.logout' , {'next_page' : '/login'}, )
    	,
    url(r'^send_tweet/$', twitter_view ),
    url(r'^send_tweet2/$', TweetView.as_view(success_url = "/send_tweet2")),
     
     ) 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#r'^blog/(?P<year>\d{4})/$'2 





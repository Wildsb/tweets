# from django.conf.urls import url
from django.urls import re_path

from django.views.generic.base import RedirectView

from .views import (
    RetweetView,
    TweetCreateView,
    TweetDeleteView,
    TweetDetailView,
    TweetListView,
    TweetUpdateView,
    )

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url="/")), 
    re_path(r'^search/$', TweetListView.as_view(), name='list'), # /tweet/
    re_path(r'^create/$', TweetCreateView.as_view(), name='create'), # /tweet/create/
    re_path(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
    re_path(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(), name='detail'), # /tweet/1/
    re_path(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update/
    re_path(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # /tweet/1/delete/
]


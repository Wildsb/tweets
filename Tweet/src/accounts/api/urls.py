from django.conf.urls import url
from django.urls import path, re_path, include

from django.views.generic.base import RedirectView

from tweets.api.views import (
    TweetListAPIView,
    )

urlpatterns = [
    re_path(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view(), name='list'), # /api/tweet/
]


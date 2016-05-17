# facebookbot/bot/urls.py

from django.conf.urls import url, include
from .views import BotView

urlpatterns = [
    url(r'7b8b093892f5be4e61dba6e6dfa19b5695273d41c9a43843f0/?$', BotView.as_view())
]
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.Chat.as_view(), name='chat'),
    #url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
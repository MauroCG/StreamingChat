from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from apps.login.views import login
from django_private_chat import urls as django_private_chat_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(django_private_chat_urls)),
    path('', login, name='login'),
]

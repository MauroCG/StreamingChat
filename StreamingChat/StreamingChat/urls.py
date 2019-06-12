from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from apps.login import views as login_views
from django_private_chat import urls as django_private_chat_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', login_views.login, name='login'),
    path('', login_views.logout, name='logout'),
    path("home/", login_views.home, name="home"),
    # python social auth
    path('', include('social_django.urls', namespace='social')),
    # django private chat
    url(r'^', include(django_private_chat_urls)),
]

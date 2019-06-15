from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from apps.login import views as login_views
from apps.chat import urls as chat_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', login_views.login, name='login'),
    path('', login_views.logout, name='logout'),
    # python social auth
    path('', include('social_django.urls', namespace='social')),
    # chat urls
    url(r'^chat/', include(chat_urls), name='chat'),
]

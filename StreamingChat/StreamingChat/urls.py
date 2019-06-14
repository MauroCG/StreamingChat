from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from apps.login import views as login_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', login_views.login, name='login'),
    path('', login_views.logout, name='logout'),
    # python social auth
    path('', include('social_django.urls', namespace='social')),
    # chat urls
    path('chat/', include('chat.urls')),
]

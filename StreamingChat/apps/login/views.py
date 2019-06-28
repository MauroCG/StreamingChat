from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.models import Session
from django.views import generic
from django.contrib.auth import get_user_model
from django.utils import timezone


class UserListView(LoginRequiredMixin, generic.ListView):

    model = get_user_model()
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'chat/users.html'
    login_url = 'admin/'


    def get_queryset(self):
        sessions = Session.objects.filter(expire_date__gte=timezone.now())
        uid_list = []

        # Build a list of user ids from that query
        for session in sessions:
            data = session.get_decoded()
            uid_list.append(data.get('_auth_user_id', None))
        print(uid_list)

        queryset = super(UserListView, self).get_queryset()
        queryset = queryset.filter(id__in=uid_list)

        return queryset

def login(request):
    return render(request, 'login/login.html')

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')
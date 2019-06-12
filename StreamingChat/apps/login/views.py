from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from braces.views import LoginRequiredMixin
from django.views import generic
from django.contrib.auth import get_user_model


class UserListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'custom_app/users.html'
	login_url = ''

def login(request):
    return render(request, 'login/login.html')


def home(request):
    return render(request, 'login/home.html')

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')
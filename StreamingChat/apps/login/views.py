from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def login(request):
    return render(request, 'login/login.html')


def home(request):
    return render(request, 'login/home.html')

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')
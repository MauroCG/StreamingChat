from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.models import Session
from django.views import generic
from django.contrib.auth import get_user_model
from django.utils import timezone
import json


def index(request):
	return render(request, 'chat/index.html', {})

def room(request, room_name):
	return render(request, 'chat/room.html', {
		'room_name_json': mark_safe(json.dumps(room_name))
		})

class Chat(LoginRequiredMixin, generic.ListView):

    model = get_user_model()
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'chat/room.html'
    login_url = 'login/'


    def get_queryset(self):
        sessions = Session.objects.filter(expire_date__gte=timezone.now())
        uid_list = []

        # Build a list of user ids from that query
        for session in sessions:
            data = session.get_decoded()
            uid_list.append(data.get('_auth_user_id', None))

        queryset = super(Chat, self).get_queryset()
        queryset = queryset.filter(id__in=uid_list)

        return queryset
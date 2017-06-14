SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'
import test3
from django.shortcuts import render_to_response,redirect
from django.utils import timezone
from .models import Appreq
from .forms import PostForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import subprocess

@csrf_exempt
def appreq(request):
    if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
            appreq = form.save()
            appreq.save()
            test3.get_credentials()
            test3.main()
    form = PostForm()
    return render_to_response( 'app/appreq.html', {'form':form}, RequestContext(request))

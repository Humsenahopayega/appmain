import create
import delete
from django.shortcuts import render_to_response,redirect
from django.utils import timezone
from .models import Appreq,User
from .forms import PostForm,RegForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import subprocess
from calendar import monthrange
from datetime import datetime
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
@csrf_exempt
def appreq(request):
    if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
            appreq = form.save(commit=False)
            appreq.published_date = timezone.now()
            appreq.save()
            return redirect('redirect')
    form = PostForm()
    return render_to_response( 'app/appreq.html', {'form':form}, RequestContext(request))
@csrf_exempt
def users(request):
    if request.method == 'POST':
      form = RegForm(request.POST)
      if form.is_valid():
          reg = form.save()
          reg.save()
    form = RegForm()
    return render_to_response( 'app/register.html', {'regform':form}, RequestContext(request))

def redirect(request):
    return render_to_response('app/redirect.html', {'redirect':redirect}, RequestContext(request))

def pagemain(request):
    return render_to_response('app/main.html', {}, RequestContext(request))

@login_required(login_url='/')
@csrf_exempt
def home(request):
    if request.method == 'POST' and 'Accept' in request.POST:
       t=request.POST.getlist('tentative')
       request.session['ID'] = t
       accept = Appreq.objects.filter(ID__in=t).update(value='1')
       create.main(request)
       tentative = Appreq.objects.filter(value='0').order_by('published_date')
       return render_to_response('app/home.html', {'request': request,
                                                'user': request.user,
                                                'tentative':tentative}, RequestContext(request))
    elif request.method == 'POST' and 'Deny' in request.POST:
       t=request.POST.getlist('tentative')
       request.session['ID'] = t
       denied = Appreq.objects.filter(ID__in=t).update(value='-1')
       tentative = Appreq.objects.filter(value='0').order_by('published_date')
       return render_to_response('app/home.html', {'request': request,
                                                'user': request.user,
                                                'tentative':tentative}, RequestContext(request))
    else:
       mail= request.user.email
       name = request.user.get_full_name()
       n= User.objects.filter(name=name)
       m=User.objects.filter(mail=mail)
       if n.exists() and m.exists():
          tentative = Appreq.objects.filter(value='0', ename=n).order_by('published_date')
          return render_to_response('app/home.html', {'request': request,
                                                'user': request.user,
                                                'tentative':tentative}, RequestContext(request))
       return render_to_response('app/nomatch.html', {}, RequestContext(request))
@csrf_exempt
@login_required(login_url='/')
def denied(request):
    if request.method == 'POST' and 'Tentative' in request.POST:
       t=request.POST.getlist('denied')
       request.session['ID'] = t
       tentative = Appreq.objects.filter(ID__in=t).update(value='0')
       denied = Appreq.objects.filter(value='-1').order_by('published_date')
       return render_to_response('app/denied.html', {'request': request,
                                                'user': request.user,
                                                'denied':denied}, RequestContext(request))
    elif request.method == 'POST' and 'Accept' in request.POST:
       t=request.POST.getlist('denied')
       request.session['ID'] = t
       accept = Appreq.objects.filter(ID__in=t).update(value='1')
       create.main(request)
       denied = Appreq.objects.filter(value='-1').order_by('published_date')
       return render_to_response('app/denied.html', {'request': request,
                                                'user': request.user,
                                                'denied':denied}, RequestContext(request))
    else:
       mail= request.user.email
       name= request.user.get_full_name()
       n= User.objects.filter(name=name)
       m=User.objects.filter(mail=mail)
       if n.exists() and m.exists():
          denied = Appreq.objects.filter(value='-1', ename=n).order_by('published_date')
          return render_to_response('app/denied.html', {'request': request,
                                                'user': request.user,
                                                'denied':denied}, RequestContext(request))
       return render_to_response('app/nomatch.html', {}, RequestContext(request))
@csrf_exempt
@login_required(login_url='/')
def accept(request):
    if request.method == 'POST' and 'Deny' in request.POST:
       t=request.POST.getlist('accept')
       request.session['ID'] = t
       denied = Appreq.objects.filter(ID__in=t).update(value='-1')
       delete.main(request)
       accept = Appreq.objects.filter(value='1').order_by('published_date')
       return render_to_response('app/accept.html', {'request': request,
                                                'user': request.user,
                                                'accept':accept}, RequestContext(request))
    elif request.method == 'POST' and 'Tentative' in request.POST:
       t=request.POST.getlist('accept')
       request.session['ID'] = t
       tentative = Appreq.objects.filter(ID__in=t).update(value='0')
       delete.main(request)
       accept = Appreq.objects.filter(value='1').order_by('published_date')
       return render_to_response('app/accept.html', {'request': request,
                                                'user': request.user,
                                                'accept':accept}, RequestContext(request))
    else:
       mail= request.user.email
       name= request.user.get_full_name()
       n= User.objects.filter(name=name)
       m=User.objects.filter(mail=mail)
       if n.exists() and m.exists():
          accept = Appreq.objects.filter(value='1',ename=n).order_by('published_date')
          return render_to_response('app/accept.html', {'request': request,
                                                'user': request.user,
                                                'accept':accept}, RequestContext(request))
       return render_to_response('app/nomatch.html', {}, RequestContext(request))
def auth_logout(request):
    logout(request)
    request.session.flush()
    return render_to_response('app/main.html', {}, RequestContext(request))

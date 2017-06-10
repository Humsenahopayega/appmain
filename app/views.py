from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Appreq
from .forms import PostForm
def appreq(request):
    if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
            appreq = form.save()
            appreq.save()
    form = PostForm()
    return render( 'app/appreq.html', {'form':form})

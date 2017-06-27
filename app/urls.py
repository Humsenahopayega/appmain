from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$', views.appreq, name='appreq'),
    url(r'^registration$', views.users, name='users'),
    url(r'^redirect$', views.redirect, name='redirect'),
    url(r'^login',views.home,name='home'),
]

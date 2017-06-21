from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.appreq, name='appreq'),
    url(r'^registration$', views.users, name='users'),
    url(r'^cal$', views.this_month, name='this_month'),
]

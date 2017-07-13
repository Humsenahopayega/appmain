from django.db import models
from django.utils import timezone
import uuid
from django.utils.html import conditional_escape as esc
from django.utils.safestring import mark_safe
from itertools import groupby

class User(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    def submit(self):
        self.save()
    def __str__(self):
        return self.name
class Appreq(models.Model):
    ename = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    ID = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    mail = models.EmailField()
    cname = models.CharField(max_length=50)
    myname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    purpose = models.TextField()
    title = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now,blank=True, null=True)
    def __unicode__(self):
        return self.ename
    def submit(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

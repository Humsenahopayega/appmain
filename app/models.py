from django.db import models
from django.utils import timezone
import uuid
from django.utils.html import conditional_escape as esc
from django.utils.safestring import mark_safe
from itertools import groupby
from calendar import HTMLCalendar, monthrange


class User(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    def submit(self):
        self.save()
    def __str__(self):
        return self.name
class Appreq(models.Model):
    ename = models.ForeignKey(User, on_delete=models.CASCADE)
    ID = models.CharField(max_length=100,primary_key=True, unique=True, default=uuid.uuid4())
    mail = models.EmailField()
    cname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    purpose = models.TextField()
    title = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    start_date = models.DateTimeField(
        default=timezone.now)
    end_date = models.DateTimeField(
        default=timezone.now)
    def __unicode__(self):
        return self.ename
    def submit(self):
        self.save()
    def __str__(self):
        return self.title

from django.db import models
from django.utils import timezone
class Appreq(models.Model):
    ename = models.ForeignKey('auth.User')
    mail = models.EmailField()
    cname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    purpose = models.TextField()
    title = models.CharField(max_length=50)
    start_date = models.DateTimeField(
        default=timezone.now)
    end_date = models.DateTimeField(
        default=timezone.now)
    def submit(self):
        self.save()
    def __str__(self):
        return self.title

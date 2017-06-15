from django.db import models
from django.utils import timezone
class User(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    def submit(self):
        self.save()
    def __str__(self):
        return self.name
class Appreq(models.Model):
    ename = models.ForeignKey(User, on_delete=models.CASCADE)
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

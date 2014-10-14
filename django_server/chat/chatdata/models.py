from django.db import models

class User(models.Model):
    user=models.CharField(max_length=100)
    addr=models.CharField(max_length=100)
    conn=models.CharField(max_length=100)
    flag=models.IntegerField(default=0)
    index=models.IntegerField(default=0)
    length=models.IntegerField(default=0)

class content(models.Model):
    message=models.CharField(max_length=200)
    user=models.ForeignKey(User)
    index=models.IntegerField(default=0)

# Create your models here.

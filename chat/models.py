from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    roomName = models.CharField(max_length=100)

class Message(models.Model):
    value = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.CharField(max_length=1000)
    roomName = models.CharField(max_length=100)
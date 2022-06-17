from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class neighbourhood(models.Model):
    zoneName = models.CharField(max_length=255, unique=True)
    zoneLocation = models.CharField(max_length=255, unique=True)
    zoneOccupants = models.IntegerField(default=0)
    zoneAdmin = models.ForeignKey(User, on_delete=models.CASCADE)
    zoneCreationDate =  models.DateTimeField(default=timezone.now)
import email
from unicodedata import name
import zoneinfo
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class neighbourhood(models.Model):
    zoneName = models.CharField(max_length=255, unique=True)
    zoneLocation = models.CharField(max_length=255, unique=True)
    zoneOccupants = models.IntegerField(default=0)
    zoneAdmin = models.ForeignKey(User, on_delete=models.CASCADE)
    zoneCreationDate =  models.DateTimeField(default=timezone.now)

    '''
    create_neigborhood()
    delete_neigborhood()
    find_neigborhood(neigborhood_id)
    update_neighborhood()
    update_occupants()
    '''


class business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    zone = models.ForeignKey(neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    contact= models.IntegerField(default = 0)

    '''
    create_business()
    delete_business()
    find_business(business_id)
    update_business()
    search business
    '''

class policeStation(models.Model):
    officers = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    zone = models.ForeignKey(neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    contact= models.IntegerField(default = 0)

    '''
    create_station()
    delete_station()
    find_station(station_id)
    update_station()
    search station
    '''

class hospital(models.Model):
    doctorsNum = models.IntegerField(default=0)
    nursesNum = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    zone = models.ForeignKey(neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    contact= models.IntegerField(default = 0)

    '''
    create_hospital()
    delete_hospital()
    find_hospital(hospital_id)
    update_hospital()
    search hospital
    '''

class school(models.Model):
    teachersNum = models.IntegerField(default=0)
    studentsNum = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    zone = models.ForeignKey(neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    contact= models.IntegerField(default = 0)

    '''
    create_school()
    delete_school()
    find_school(school_id)
    update_school()
    search school
    '''
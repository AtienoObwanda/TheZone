from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse



class hood(models.Model):
    zoneName = models.CharField(max_length=255, unique=True)
    zoneLocation = models.CharField(max_length=255, unique=True)
    zoneOccupants = models.IntegerField(default=0)
    zoneAdmin = models.ForeignKey(User, on_delete=models.CASCADE)
    zoneCreationDate =  models.DateTimeField(default=timezone.now)
    zoneImage = models.ImageField(default='default.png',upload_to='zonePics')

    def __str__(self):
            return str (self.zoneName)

    def get_absolute_url(self):
        return reverse('joinhood')


    # create
    def createHood(self):
        self.save()

    # delete
    def deleteHood(self):
        self.delete()

    # find_station(station_id)
    @classmethod
    def findHood(cls, hood_id):
        hood= hood.objects.filter(hood_id=hood_id).all()

    # update
    def updateHood(self,  new_zoneName):
        self.zoneName = new_zoneName
        self.save()

    def updateOccupants(self,  new_zoneOccupants):
        self.zoneOccupants = new_zoneOccupants
        self.save()

    @classmethod
    def getAllZones(cls):
        allZones= cls.objects.all()
        return allZones

 

class business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bizName = models.CharField(max_length=255)
    zone = models.ForeignKey(hood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    contact= models.IntegerField(default = 0)
    def __str__(self):
            return str (self.bizName)

    def get_absolute_url(self):
        return reverse('dashboard')

    # create_business()
    def createBusiness(self):
        self.save()

    # delete_business()
    def deleteBusiness(self):
        self.delete()

    # find_business(business_id)
    @classmethod
    def findBusiness(cls, business_id):
        business= business.objects.filter(business_id=business_id).all()

    # update_business()
    def updateBusiness(self,  new_bizName):
        self.bizName = new_bizName
        self.save()

    # search business
    @classmethod
    def searchBusiness(cls, bizName):
        return cls.objects.filter(business__bizName__icontains=bizName).all()

    @classmethod
    def getAllBusinesses(cls):
        allBusiness = cls.objects.all()
        return allBusiness

    @classmethod
    def getZoneBizz(cls, zone_id):
        zoneBiz = business.objects.filter(zone_id=zone_id).all()
        return zoneBiz


   

class policeStation(models.Model):
    officers = models.IntegerField(default=0)
    stationName = models.CharField(max_length=255)
    zone = models.ForeignKey(hood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    contact= models.IntegerField(default = 0)
    def __str__(self):
            return str (self.stationName)

    def get_absolute_url(self):
        return reverse('dashboard')

    # create
    def createStation(self):
        self.save()

    # delete
    def deleteStation(self):
        self.delete()

    # find_station(station_id)
    @classmethod
    def findStation(cls, policeStation_id):
        business= business.objects.filter(policeStation_id=policeStation_id).all()

    # update
    def updateStation(self,  new_stationName):
        self.stationName = new_stationName
        self.save()

    @classmethod
    def getAllStations(cls):
        allStation= cls.objects.all()
        return allStation

    @classmethod
    def getZoneStations(cls, zone_id):
        zoneStation= policeStation.objects.filter(zone_id=zone_id).all()
        return zoneStation

class hospital(models.Model):
    doctorsNum = models.IntegerField(default=0)
    nursesNum = models.IntegerField(default=0)
    hName = models.CharField(max_length=255)
    zone = models.ForeignKey(hood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    contact= models.IntegerField(default = 0)
    def __str__(self):
            return str (self.hName)

    def get_absolute_url(self):
            return reverse('dashboard')

    # create
    def createHospital(self):
        self.save()

    # delete
    def deleteHospital(self):
        self.delete()

    # find_station(station_id)
    @classmethod
    def findHospital(cls, hospital_id):
        hospital= hospital.objects.filter(hospital_id=hospital_id).all()

    # update
    def updateHospital(self,  new_hName):
        self.hName = new_hName
        self.save()

    @classmethod
    def getAllHospitals(cls):
        allHospitals= cls.objects.all()
        return allHospitals

    @classmethod
    def getZoneHospitals(cls, zone_id):
        zoneHospital= policeStation.objects.filter(zone_id=zone_id).all()
        return zoneHospital

class school(models.Model):
    teachersNum = models.IntegerField(default=0)
    studentsNum = models.IntegerField(default=0)
    schlName = models.CharField(max_length=255)
    zone = models.ForeignKey(hood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    contact= models.IntegerField(default = 0)
    def __str__(self):
            return str (self.schlName)

    def get_absolute_url(self):
            return reverse('dashboard')
    # create
    def createSchool(self):
        self.save()

    # delete
    def deleteSchool(self):
        self.delete()

    # find_station(station_id)
    @classmethod
    def findSchool(cls, school_id):
        business= business.objects.filter(school_id=school_id).all()

    # update
    def updateSchool(self,  new_schlName):
        self.schlName = new_schlName
        self.save()

    @classmethod
    def getAllSchool(cls):
        allSchool = cls.objects.all()
        return allSchool

    @classmethod
    def getZoneSchool(cls, zone_id):
        zoneSchool= school.objects.filter(zone_id=zone_id).all()
        return zoneSchool

class Post(models.Model):
    title = models.CharField(max_length=30, blank=True)
    post=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    zone=models.ForeignKey(hood,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('dashboard')
    
    def __str__(self):
            return str (self.title)

    # create
    def createPost(self):
        self.save()

    # delete
    def deletePost(self):
        self.delete()

    # find_station(station_id)
    @classmethod
    def findPost(cls, post_id):
        post= Post.objects.filter(post_id=post_id).all()
        return post

    # update
    def updatePost(self,  new_post):
        self.post = new_post
        self.save()

  

from django.test import TestCase
from . models import *
from datetime import date, datetime
from django.contrib.auth.models import User


class hoodTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(username='testuser' , password='testpassword')
        self.test_user.save()

        self.test_hood = hood(zoneName='Dite', zoneLocation='Eastlands', zoneOccupants  =12, zoneAdmin=self.test_user, zoneCreationDate=datetime.now())

    def test_instance(self):
        self.assertTrue(isinstance(self.test_hood, hood))

    def test_createHood(self):
        self.test_hood.createHood()
        self.assertEqual(len(hood.objects.all()),1)

    def test_findHood(self):
        test_id = 1
        getHood=hood.objects.filter(id=test_id)
        self.assertEqual(len(getHood),0)

    def test_updateHood(self):
        self.test_hood.updateHood(new_zoneName='DeepInTheEast')
        self.test_hood.createHood()

    def test_updateOccupants(self):
        self.test_hood.updateOccupants(new_zoneOccupants=12)
        self.test_hood.createHood()

    def test_getAllZones(self):
        allZones= hood.objects.all()
        return allZones



    def tearDown(self):
        self.test_user.delete()
        hood.objects.all().delete()
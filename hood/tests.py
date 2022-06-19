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


class businessTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(username='testuser' , password='testpassword')
        self.test_user.save()

        self.test_hood = hood(zoneName='Dite', zoneLocation='Eastlands', zoneOccupants  =12, zoneAdmin=self.test_user, zoneCreationDate=datetime.now())
        self.test_hood.save()

        self.test_business = business(owner=self.test_user, bizName='Shop Test', zone=self.test_hood, email="test@example.gmail.com", contact = 000000 )


    def test_instance(self):
        self.assertTrue(isinstance(self.test_business, business))

    def test_createBusiness(self):
        self.test_business.createBusiness()
        self.assertEqual(len(business.objects.all()),1)

    def test_findBusiness(self):
        test_id = 1
        getBusiness=business.objects.filter(id=test_id)
        self.assertEqual(len(getBusiness),0)

    def test_updateBusiness(self):
        self.test_business.updateBusiness(new_bizName='DITE Shops')
        self.test_business.createBusiness()

    def test_getAllBusinesses(self):
        allBusiness= business.objects.all()
        return allBusiness

    def tearDown(self):
        self.test_user.delete()
        self.test_hood.delete()
        business.objects.all().delete()


class PostTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(username='testuser' , password='testpassword')
        self.test_user.save()

        self.test_hood = hood(zoneName='Dite', zoneLocation='Eastlands', zoneOccupants  =12, zoneAdmin=self.test_user, zoneCreationDate=datetime.now())
        self.test_hood.save()

        self.test_post = Post(author=self.test_user, title='Test Post',post='post test', zone=self.test_hood)


    def test_instance(self):
        self.assertTrue(isinstance(self.test_post, Post))

    def test_createPost(self):
        self.test_post.createPost()
        self.assertEqual(len(Post.objects.all()),1)

    def test_findPost(self):
        test_id = 1
        getPost=Post.objects.filter(id=test_id)
        self.assertEqual(len(getPost),0)

    def test_updatePost(self):
        self.test_post.updatePost(new_post='Test Update')
        self.test_post.createPost()

    def test_getAllPosts(self):
        allPosts= Post.objects.all()
        return allPosts

    def tearDown(self):
        self.test_user.delete()
        self.test_hood.delete()
        Post.objects.all().delete()

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

from hood.models import hood



class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    zone = models.ForeignKey(hood, on_delete=models.CASCADE, null=True)
    profileImage = models.ImageField(default='default.png',upload_to='projectPics')
    phone= models.IntegerField(blank=True,null=True, default=0)
    idNum= models.IntegerField(blank=True, null=True, default=0)



    def __str__(self):
        return f'{self.user.username}profile'

#   Signals
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        
        instance.profile.save()


#   methods:
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self, new_bio):
        self.bio = new_bio
        self.save()

    def update_image(self, user_id, new_image):
        user = User.objects.get(id=user_id)
        self.photo = new_image
        self.save()

   
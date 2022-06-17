from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

from app.models import hood



class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    zone = models.ForeignKey(hood, on_delete=models.CASCADE)
    # country = models.CharField(max_length=50)
    profileImage = models.ImageField(default='default.png',upload_to='projectPics')
    bio=models.TextField(max_length=50, blank=True, default=f'The Zone Community')
    phone= models.IntegerField()
    idNum= models.IntegerField()



    def __str__(self):
        return f'{self.user.username}profile'

#   Signals
    def save(self, *args,**kwargs):
        super(Profile, self).save(*args,**kwargs)
 
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size=(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

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

   
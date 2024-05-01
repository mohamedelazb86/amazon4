from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user=models.OneToOneField(User,related_name='profile_user',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photo_user')
    code=models.CharField(max_length=50,default=generate_code)


    def __Str__(self):
        return str(self.user)
    
@receiver(post_save,sender=User)    
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )


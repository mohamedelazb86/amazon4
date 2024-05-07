from django.db import models
from django.utils.translation import gettext_lazy as _


class Setting(models.Model):
    name=models.CharField(max_length=120,verbose_name=_('name'))
    logo=models.ImageField(upload_to='logo')
    subtitle=models.TextField(max_length=1500)
    call_us=models.CharField(max_length=50)
    email_us=models.CharField(max_length=75)
    phones=models.TextField(max_length=200)
    address=models.TextField(max_length=200)
    andriod_app=models.URLField(null=True,blank=True)
    ios_app=models.URLField(null=True,blank=True)
    facebook=models.URLField(null=True,blank=True)
    youtube=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    


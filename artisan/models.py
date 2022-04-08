from django.db import models


# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

#from django.contrib.auth import get_user_model

#User = get_user_model()
LAGOS_CHOICES =(
    ('Alimosho' ,'Alimosho'),
    ('Ajeromi-Ifelodun' ,'Ajeromi-Ifelodun'),
    ('Kosofe' ,'Kosofe'),
    ('Mushin' ,'Mushin'),
    ('Oshodi-Isolo' ,'Oshodi-Isolo'),
    ('Ojo' ,'Ojo'),
    ('Ikorodu' ,'Ikorodu'),
    ('Surulere' ,'Surulere'),
    ('Agege' ,'Agege'),
    ('Ifako-Ijaiye' ,'Ifako-Ijaiye'),
    ('Somolu' ,'Somolu'),
    ('Amuwo-Odofin' ,'Amuwo-Odofin'),

    ('Lagos Mainland' ,'Lagos Mainland'),
    ('Ikeja' ,'Ikeja'),
     ('Eti-Osa' ,'Eti-Osa'),
    ('Badagry' ,'Badagry'),
    ('Apapa' ,'Apapa'), 
    ('Lagos Island' ,'Lagos Island'),
    ('Epe' ,'Epe'), 
    ('Ibeju-Lekki' ,'Ibeju-Lekki'), 
    ('Ikoyi-obalende' ,'Ikoyi-obalende'),

)

LAGOS_ZONES =(
    ('Alimosho' ,'Alimosho'),
    ('Ajeromi-Ifelodun' ,'Ajeromi-Ifelodun'),
    ('Kosofe' ,'Kosofe'),
    ('Mushin' ,'Mushin'),
    ('Oshodi-Isolo' ,'Oshodi-Isolo'),
    ('Ojo' ,'Ojo'),
    ('Ikorodu' ,'Ikorodu'),
    ('Surulere' ,'Surulere'),
    ('Agege' ,'Agege'),
    ('Ifako-Ijaiye' ,'Ifako-Ijaiye'),
    ('Somolu' ,'Somolu'),
    ('Amuwo-Odofin' ,'Amuwo-Odofin'),

    ('Lagos Mainland' ,'Lagos Mainland'),
    ('Ikeja' ,'Ikeja'),
     ('Eti-Osa' ,'Eti-Osa'),
    ('Badagry' ,'Badagry'),
    ('Apapa' ,'Apapa'), 
    ('Lagos Island' ,'Lagos Island'),
    ('Epe' ,'Epe'), 
    ('Ibeju-Lekki' ,'Ibeju-Lekki'), 
    ('Ikoyi-obalende' ,'Ikoyi-obalende'),

)
# Create your models here.

class Area(models.Model):
   area_code = models.CharField(max_length=7)
   location = models.CharField(max_length=100,unique=True)
    
   def __str__(self):
      return self.location

   class Meta:
      verbose_name_plural = "Area"





#class Worker(models.Model):
   
   #user = models.OneToOneField(User,null=True,blank=True, on_delete= models.SET_NULL,related_name='worker')
   #location = models.CharField(max_length=50,null=False,blank=True, choices=LAGOS_CHOICES,default='')
   #location = models.ForeignKey(Area ,on_delete =models.CASCADE ,null=True,blank=True)

   #place = models.ForeignKey(Area,blank=True,null=False, on_delete=models.CASCADE,default='')
   #artisan = models.CharField(default=True)
   #loc = models.CharField(max_length=50,null=False, blank=True, choices=LAGOS_ZONES,default='')
   #address = models.CharField(max_length=200, null=True)
  # phone = models.CharField(max_length=15, null=True, unique=True)
  # nin =  models.CharField(max_length=20, null=True, unique = True)
   #date_created = models.DateTimeField(auto_now_add=True, null=True)

   #def __str__(self):
    #  return str(self.user.username)

    

#image resize
#class Profile(models.Model):
    # ...
   # def save(self, *args, **kwargs):
      #  super().save(*args, **kwargs)
       # img = Image.open(self.pic.path)
       # if img.mode in ("RGBA", "P"): img = img.convert("RGB")
       # if img.height > 300 or img.width > 300:
        #    output_size = (300, 300)
         #   img.thumbnail(output_size)
          #  img.save(self.pic.path)   






class Artisan(models.Model):
   
   user = models.OneToOneField(User,null=True,blank=True, on_delete= models.SET_NULL,related_name='artisan')
   nin =  models.CharField(max_length=20, null=True, unique = True)
   location = models.ForeignKey(Area ,on_delete =models.CASCADE ,null=True,blank=True)
   
   address = models.CharField(max_length=200, null=True)
   phone = models.CharField(max_length=15, null=True,unique=True)
   profession_name = models.CharField(max_length=20, null=True, unique = False)
 
   profile_img = CloudinaryField(blank=True,null=True)

   #date_created = models.DateTimeField(auto_now_add=True, null=True)
   date_created = models.DateField(auto_now_add = True, null=True, blank=True)


   def __str__(self):
      return str(self.user.username)

      

      #python manage.py migrate location --database=location_db


  #this steps sould my proble here
  # heroku run bash
#python manage.py makemigrations
#python manage.py migrate    
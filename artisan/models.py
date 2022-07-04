from http import client
from pydoc import describe
from django.db import models


# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from products.models import *

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






class Artisan(models.Model):

  user = models.OneToOneField(User,null=True,blank=True, on_delete= models.SET_NULL,related_name='artisan')
  nin =  models.CharField(max_length=20, null=True, unique = True)
  location = models.ForeignKey(Area ,on_delete =models.CASCADE ,null=True,blank=True)
   
  address = models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=15, null=True,unique=True)
  #profession_name = models.CharField(max_length=200, null=True, unique = False)
  profession_name = models.ForeignKey('products.Product' ,on_delete =models.CASCADE ,null=True,blank=True,unique = False)
 
  profile_img = CloudinaryField(blank=True,null=True)

   #date_created = models.DateTimeField(auto_now_add=True, null=True)
  date_created = models.DateField(auto_now_add = True, null=True, blank=True)


  def __str__(self):
    return str(self.user.username)

      



class CompletedJob(models.Model):
  
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  job_name =  models.CharField(max_length=200, null=True, unique = True)
  description = models.CharField(max_length=200, null=True, unique = True)
  category = models.CharField(max_length=200, null=True, unique = False)
  client = models.CharField(max_length=200, null=True)
  address = models.CharField(max_length=200, null=True)
  date = models.DateField(auto_now_add = True, null=True, blank=True)
  pay =models.FloatField(default=00.00)
   



  def __str__(self):
      return str(self.user.username)




class ViewedJob(models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  #user = models.OneToOneField(User,null=True,blank=True, on_delete= models.SET_NULL,related_name='jobview')
  job_name =  models.CharField(max_length=200, null=True, unique = False)
  job_order_id =models.PositiveIntegerField(null=True,blank=True)
  category = models.CharField(max_length=200, null=True, unique = False)
  description = models.CharField(max_length=200, null=True, unique = False)
  client = models.CharField(max_length=200, null=True, unique = False)
  address = models.CharField(max_length=200, null=True, unique = False)
  date = models.DateField(auto_now_add = True, null=True, blank=True)
  price = models.FloatField(default=00.00, null=True, unique = False)
  phone = models.CharField(max_length=15, null=True, unique = False)
  accepted = models.CharField(max_length=100, null=True,blank=True,default='No')
  accepted_date = models.DateField(auto_now_add = True, null=True, blank=True)
  work_done = models.BooleanField(default=False,null=True)
  #completed_job  =  models.BooleanField(null=True,blank=True,default=False)


  def __str__(self):
      return str(self.user.username)




class BankDetails(models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  bank_name =  models.CharField(max_length=200, null=True, unique = True)
  account_type = models.CharField(max_length=200, null=True, unique = True)
  account_number = models.CharField(max_length=200, null=True, unique = False)
 
 
  payment_date = models.DateField(auto_now_add = True, null=True, blank=True)
  amount =models.FloatField(default=00.00)
   



  def __str__(self):
      return str(self.user.username)

  class Meta:
      verbose_name_plural = "BankDetails"    





   

   
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser



lagos_choices ={
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

}





class Customer(models.Model):

    user = models.OneToOneField(User,null=True,blank=True, on_delete= models.SET_NULL,related_name='details')
    phone = models.CharField(max_length=15, null=True,unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
   
    
    class Meta:
        verbose_name_plural = 'Customer' 

    def __str__(self):
        return str(self.user.username)

   
        
        



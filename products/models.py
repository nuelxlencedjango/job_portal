from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from artisan.models import Artisan

User = get_user_model()
from cloudinary.models import CloudinaryField







class Category(models.Model):
    title=models.CharField(max_length=100)
 
    class Meta:
        verbose_name_plural='Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title







# Product Model
class Product(models.Model):

   STATUS = (
        	('Pending', 'Pending'),
            #('On-going', 'On-going'),
        	('Paid', 'Paid'),
            ('comepleted', 'Completed'),
        	)
    
   name=models.CharField(max_length=200)
 
   desc=models.TextField()
   category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
   price = models.FloatField(default=00.00)

   img = CloudinaryField(blank=True,null=True)

   location = models.ForeignKey('artisan.Area' ,on_delete =models.CASCADE ,null=True,blank=True)

   status = models.CharField(max_length=200, null=True, choices=STATUS,default='Pending')
   date_created = models.DateTimeField(auto_now_add=True, null=True)
  

   class Meta:
      verbose_name_plural='Products'
  
   def clean(self):
        self.name = self.name.capitalize()     

   def get_add_to_cart(self):
      return reverse('product:add-to-cart' ,kwargs={
            "pk":self.pk
        })

   def __str__(self):
      return self.name   



class OrderItem(models.Model):

   user = models.ForeignKey(User, on_delete=models.CASCADE)
   ordered = models.BooleanField(default=False)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.IntegerField(default =1)
   img = CloudinaryField(blank=True,null=True)
   status = models.CharField(max_length=200, null=True, blank=True, default='Pending')
   description=models.TextField(max_length=100,null=True,blank=True)
   address = models.CharField(max_length=300, null=True,blank=True)
   artisan_assigned = models.ManyToManyField('artisan.Artisan' ,blank=True) 
   date_created = models.DateField(auto_now_add = True, null=True, blank=True)
   accepted = models.CharField(max_length=100, null=True,blank=True,default='No')
   accepted_date = models.DateField(auto_now_add = True, null=True, blank=True)
   work_done = models.BooleanField(default=False,null=True)
  
   class Meta:
      verbose_name_plural='Orderitem'
       
      ordering = ['-date_created']

   def __str__(self):
      return f"{self.quantity} of {self.product.name}"

   def get_total_item_price(self):
      return self.quantity * self.product.price

   def get_final_price(self):
      return self.get_total_item_price() 

   def vat(self):
      return self.get_vat()   

   def get_service_rate(self):
      amount = (self.product.price * 75/100)
      return amount   

  
     
class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   items = models.ManyToManyField(OrderItem)
   start_date = models.DateTimeField(auto_now_add=True)
   ordered_date = models.DateTimeField()
   ordered = models.BooleanField(default=False)
   order_id = models.CharField(max_length=50,unique=True, default =None,blank=True,null=True)
   datetime_ofpayment =models.DateTimeField(auto_now_add=True)
   artisanName = models.CharField(max_length=200,unique=False,blank=True,null=True)
   payment_id = models.CharField(max_length=50, blank=True,null=True)
   def save(self, *args,**kwargs):
      if self.order_id is None and self.datetime_ofpayment and self.id:
         self.order_id = self.datetime_ofpayment.strftime('PAY2ME%Y%m%dODR') + str(self.id)

      return super().save(*args, **kwargs)

   def __str__(self):
      return self.user.username

   class Meta:
      verbose_name_plural='Order'

   def get_total_price(self):
      total =0
      for order_item in self.items.all():
         total +=order_item.get_final_price()
      return total

   def get_total_count(self):
      order =Order.objects.get(pk=self.pk)
      return order.items.count()  

   def get_vat(self):
      return (self.get_total_price() * 5)/100

   def get_final_amount(self):
      return (self.get_total_price() + self.get_vat())


                
class ContactUs(models.Model):
   name = models.CharField(max_length=100) 
   email = models.EmailField(unique = False) 
   phone = models.CharField(max_length=20) 
   message = models.TextField(max_length=100)

   class Meta:
      verbose_name_plural = "Contact Us"

   def __str__(self):
      return self.name        



class PaymentDetail(models.Model):
   name = models.CharField(max_length=100) 
   phone = models.CharField(max_length=20)
   email = models.EmailField(unique = False) 
   amount = models.CharField(max_length=100) 
   class Meta:
      verbose_name_plural = "Payment Detail"

   def __str__(self):
      return self.name  



class OurLocations(models.Model):
   name = models.CharField(max_length=100) 
   date_added = models.DateTimeField(auto_now_add=True,auto_now=False)
 
   class Meta:
      verbose_name_plural = "OurLocation"

   def __str__(self):
      return self.name  



class ServiceRequest(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   ordered = models.BooleanField(default=False)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   number_of_workers = models.IntegerField(default =1)
   img = CloudinaryField(blank=True,null=True)
   status = models.CharField(max_length=200, null=True, blank=True, default='Pending')
   description=models.TextField(max_length=100,null=True,blank=True)
   address = models.CharField(max_length=300, null=True,blank=True)
   artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE,null=True,blank=True)
   date_created = models.DateField(auto_now_add = True, null=True, blank=True)

   accepted = models.CharField(max_length=100, null=True,blank=True,default='No')
   
   location = models.ForeignKey('artisan.Area' ,on_delete =models.CASCADE ,null=True,blank=True)
   accepted_date = models.DateField(auto_now_add = True, null=True, blank=True)
   work_done = models.BooleanField(default=False,null=True)
  
   
   class Meta:
      verbose_name_plural='ServiceRequest'
       
      ordering = ['-date_created']

   def __str__(self):
      return f"{self.number_of_workers} of {self.product.name}"

   def get_total_item_price(self):
      return (self.number_of_workers * self.product.price)

   def get_final_price(self):
      return self.get_total_item_price() 

   def vat(self):
      return self.get_vat()   

   def get_service_rate(self):
      amount = (self.product.price * 75/100)
      return amount      



class ServiceOrder(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   items = models.ManyToManyField(ServiceRequest)
   start_date = models.DateTimeField(auto_now_add=True)
   ordered_date = models.DateTimeField()
   ordered = models.BooleanField(default=False)
   order_id = models.CharField(max_length=50,unique=True, default =None,blank=True,null=True)
   datetime_ofpayment =models.DateTimeField(auto_now_add=True)
   artisanName = models.CharField(max_length=200,unique=False,blank=True,null=True)
   payment_id = models.CharField(max_length=50, blank=True,null=True)


   class Meta:
      verbose_name_plural='ServiceOrder'
      ordering = ['-ordered_date']
   

   def save(self, *args,**kwargs):
      if self.order_id is None and self.datetime_ofpayment and self.id:
         self.order_id = self.datetime_ofpayment.strftime('PAY2ME%Y%m%dODR') + str(self.id)

      return super().save(*args, **kwargs)

   def __str__(self):
      return self.user.username

   
   def get_total_price(self):
      total =0
      for order_item in self.items.all():
               total +=order_item.get_final_price()
               

      return total

   def get_total_count(self):
      order =Order.objects.get(pk=self.pk)
      return order.items.count()  

   
   def get_vat(self):
      return (self.get_total_price() * 5)/100


   def get_final_amount(self):
      return (self.get_total_price() + self.get_vat())



class Services(models.Model):
   service_name = models.CharField(max_length=200,blank=True,null=True)
   desc1 = models.CharField(max_length=200, blank=True,null=True)
   desc2 = models.CharField(max_length=200, blank=True,null=True)
   desc3 = models.CharField(max_length=200, blank=True,null=True)

   def __str__(self):
      return self.service_name

   
   class Meta:
      verbose_name_plural='Services'    



class TrainStaff(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name =  models.CharField(max_length=200, null=True, blank=True)
   type_of_service =  models.CharField(max_length=200, null=True, blank=True)
   number_of_people = models.IntegerField(default =1)
   status = models.CharField(max_length=200, null=True, blank=True, default='Pending')
   description=models.TextField(max_length=200,null=True,blank=True)
   address = models.CharField(max_length=200, null=True,blank=True)
   date_created = models.DateField(auto_now_add = True, null=True, blank=True)
   work_done = models.BooleanField(default=False,null=True)
   location = models.ForeignKey('artisan.Area' ,on_delete =models.CASCADE ,null=True,blank=True)

   class Meta:
      verbose_name_plural='TrainStaff'
       
      ordering = ['-date_created']


   def __str__(self):
      return f"{self.number_of_people} of {self.type_of_service}"

   
   

class PostJob(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   paid = models.BooleanField(default=False)
   number_of_people = models.IntegerField(default =1)
   services = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
   status = models.CharField(max_length=200, null=True, blank=True, default='Pending')
   description=models.TextField(max_length=200,null=True,blank=True)
   address = models.CharField(max_length=200, null=True,blank=True)
   artisan_assigned = models.ManyToManyField('artisan.Artisan' ,blank=True) 
   date_created = models.DateField(auto_now_add = True, null=True, blank=True)
   accepted = models.CharField(max_length=100, null=True,blank=True,default='No')
   accepted_date = models.DateField(auto_now_add = True, null=True, blank=True)
   work_done = models.BooleanField(default=False,null=True)
   location = models.ForeignKey('artisan.Area' ,on_delete =models.CASCADE ,null=True,blank=True)

   class Meta:
      verbose_name_plural='PostJob'
       
      ordering = ['-date_created']


   def __str__(self):
      return f"{self.number_of_people} of {self.services}"

   def get_total_item_price(self):
      return self.number_of_people * self.services.price

   def get_final_price(self):
      return self.get_total_item_price() 

   def vat(self):
      return self.get_vat()   

   def get_service_rate(self):
      amount = (self.price * 75/100)
      return amount   

   
   def get_total_price(self):

      total =0
      for order_item in self.items.all():
               total +=order_item.get_final_price()
      return total

 
   




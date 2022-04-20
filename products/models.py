from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from artisan.models import Artisan

User = get_user_model()


from cloudinary.models import CloudinaryField







#class Production(models.Model):#
#   CATEGORY = (
  #       ('Indoor', 'Indoor'),
   #      ('OutDoor', 'Out Door'),
   #      ) 

  # name = models.CharField(max_length=200, null=True)
  # price = models.DecimalField(max_digits=7,decimal_places=2, null=True)
  # digital = models.BooleanField(default=False,null=True,blank=True)
  # category = models.CharField(max_length=200, null=True, choices=CATEGORY)
  # description = models.CharField(max_length=200, null=True, blank=True)
  # date_created = models.DateTimeField(auto_now_add=True, null=True)
   #tags = models.ManyToManyField(Tag)
   #image = models.ImageField(blank=True,null=True,upload_to='images/')
  # image = CloudinaryField(blank=True,null=True)

  # def __str__(self):
   #   return self.name

  # @property
  # def imageUrl(self):
   #   try:
   #      url = self.image.url
   #   except:
   #      url = ''
   #   return url  




#class Orders(models.Model):#
#   STATUS = (
 #        ('Pending', 'Pending'),
#         ('Out for delivery', 'Out for delivery'),
 #        ('Delivered', 'Delivered'),
 #        )
    
  # customer = models.ForeignKey(User, on_delete=models.CASCADE,blank= True, null=True)
   #customer = models.ForeignKey('account.Customer', null=True, on_delete= models.SET_NULL)
  # product = models.ForeignKey(Production, null=True, on_delete= models.SET_NULL)
  # date_created = models.DateTimeField(auto_now_add=True, null=True)
  # status = models.CharField(max_length=200, null=True, choices=STATUS)
  # note = models.CharField(max_length=1000, null=True)
  # complete = models.BooleanField(default=False,blank=False,null=False)
  # transaction_id = models.CharField(max_length=20,null=True,blank=True)


 #  class Meta:
  #    verbose_name_plural='Orders'

  # def __str__(self):
  #    return  self.customer.username 
    
  # @property 
   #def get_cart_total(self):
   #   orderitems = self.orderitem_set.all()
   #   total = sum([item.get_total for item in orderitems ])  

    #  return total 

  # @property
  # def get_cart_items(self):
   #   orderitems = self.orderitem_set.all()
   #   total = sum([item.quantity for item in orderitems])

   
  # @property
  # def shipping(self):
   #   shipping =False
   #   orderitems = self.orderitem_set.all()
    #  for i in orderitems:
     #    if i.product.digital == False:
     #       shipping = True
    #  return shipping
         

#class OrderItems(models.Model):  #

  # product = models.ForeignKey(Production, null=True, on_delete= models.SET_NULL)
  # orders = models.ForeignKey(Orders, null=True, on_delete= models.SET_NULL)
  # quantity = models.IntegerField(default=0, null=True ,blank=True)
 #  date_added = models.DateTimeField(auto_now_add=True) 


  # class Meta:
  #    verbose_name_plural='Orderitems'

   #def __str__(self):
    #  return self.product.name




#class Carts(models.Model):

  # items = models.ManyToManyField(OrderItems,null=True,blank=True)
  # products = models.ManyToManyField(Production,null=True,blank=True)
  # total = models.DecimalField(max_digits=100, decimal_places=2,default=0.00)
  # timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
  # update = models.DateTimeField(auto_now_add=True,auto_now=False)
  # active = models.BooleanField(default=False)

    
  # def __str__(self):
  #    return "Cart Id: %s" %(self.id)

   
  # class Meta:
   #   verbose_name_plural='Carts'     







class Category(models.Model):
    title=models.CharField(max_length=100)
    #image=models.ImageField(upload_to="cat_imgs/")

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
    
   price = models.FloatField(default=0.00)
   #product_available_count =models.IntegerField(default=0)
   img = CloudinaryField(blank=True,null=True)

   location = models.ForeignKey('artisan.Area' ,on_delete =models.CASCADE ,null=True,blank=True)

   status = models.CharField(max_length=200, null=True, choices=STATUS,default='Pending')
   date_created = models.DateTimeField(auto_now_add=True, null=True)
    #brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    #status=models.BooleanField(default=True)
    #is_featured=models.BooleanField(default=False)

   class Meta:
      verbose_name_plural='Products'

   #def get_absolute_url(self):
      #return reverse('product:add-to-cart' ,kwargs={
       #     "pk":self.pk
        #})   

   def get_add_to_cart(self):
      return reverse('product:add-to-cart' ,kwargs={
            "pk":self.pk
        })

   #def get_add_to_shop_url(self):
      #return reverse('product:add-to-cart' ,kwargs={
       #     "pk":self.pk
       # })     
    
    #@property
    #def img_url(self):
       # if self.img and hasattr(self.img, 'url'):
       #     return self.img.url

      

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
   #location = models.ForeignKey('artsans.Area' ,on_delete =models.CASCADE ,null=True,blank=True)
   address = models.CharField(max_length=300, null=True,blank=True)
   artisan_assigned =  models.ForeignKey(Artisan, on_delete=models.CASCADE,null=True,blank=True) 
   date_created = models.DateField(auto_now_add = True, null=True, blank=True)
   #payment_id
   
   class Meta:
      verbose_name_plural='Orderitem'

   def __str__(self):
      return f"{self.quantity} of {self.product.name}"

   def get_total_item_price(self):
      return self.quantity * self.product.price

   def get_final_price(self):
      return self.get_total_item_price() 

   def vat(self):
      return self.get_vat()   
     










class Order(models.Model):
   #date=models.DateField(auto_now=False,auto_now_add=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   items = models.ManyToManyField(OrderItem)
   start_date = models.DateTimeField(auto_now_add=True)
   ordered_date = models.DateTimeField()
   ordered = models.BooleanField(default=False)
   order_id = models.CharField(max_length=50,unique=True, default =None,blank=True,null=True)
   datetime_ofpayment =models.DateTimeField(auto_now_add=True)
   order_delivered = models.BooleanField(default=False)
   order_received = models.BooleanField(default=False)
    
   razorpay_order_id = models.CharField(max_length=50, blank=True,null=True)

   payment_id = models.CharField(max_length=50, blank=True,null=True)

   razorpay_signature = models.CharField(max_length=50, blank=True,null=True)

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

                
   
class PaidServices(models.Model):
   pass




class Cart(models.Model):
   items = models.ManyToManyField(OrderItem)
   products = models.ManyToManyField(Product)
   total = models.DecimalField(max_digits=100, decimal_places=2,default=0.00)
   timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
   update = models.DateTimeField(auto_now_add=True,auto_now=False)
   active = models.BooleanField(default=False)

    
   def __str__(self):
      return "Cart Id: %s" %(self.id)
   
   class Meta:
      verbose_name_plural='Cart'   



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
      verbose_name_plural = "Contact Us"

   def __str__(self):
      return self.name  


#to be removed
#class CheckoutAddress(models.Model):
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  # street_address = models.CharField(max_length=100) 
   #appartment_address = models.CharField(max_length=100) 
   #country = CountryField(multiple=False)
   #zip_code = models.CharField(max_length=100) 
   
    
   #def __str__(self):
   #   return self.user.username
   
  
#import os
#os.getcwd()










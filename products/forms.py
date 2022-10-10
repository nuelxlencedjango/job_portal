
from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import *



class ProductForm(forms.ModelForm):
    
  
    class Meta:
        model = Product
        fields =('name','desc' ,'location')

    def __init__(self ,*args ,**kwargs):

        super(ProductForm ,self).__init__(*args ,**kwargs)
        self.fields['location'].empty_label ='select your zone'      



class OrderItemForm(forms.ModelForm):
     class Meta:
        model = OrderItem
        fields =('product','quantity','address' ,'description')




class  PostJobForm(forms.ModelForm):
    class Meta:
        model = PostJob
        fields =('services','number_of_people' ,'description','location','address')

    def __init__(self ,*args ,**kwargs):

        super(PostJobForm ,self).__init__(*args ,**kwargs)
        self.fields['location'].empty_label ='select location'

 

class  PostServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields =('product','number_of_workers','description','address','location')


    def __init__(self ,*args ,**kwargs):

        super(PostServiceForm ,self).__init__(*args ,**kwargs)
        self.fields['product'].empty_label ='Select services you want'



class  TrainingStaff(forms.ModelForm):
    class Meta:
        model = TrainStaff
        fields =('name','number_of_people','description','address','type_of_service','location')

    def __init__(self ,*args ,**kwargs):

        super(TrainingStaff ,self).__init__(*args ,**kwargs)
        self.fields['location'].empty_label ='Select location'
        


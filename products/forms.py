
from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import *



class ProductForm(forms.ModelForm):
    
    #location =forms.CharField(required=True)
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self ,*args ,**kwargs):

        super(ProductForm ,self).__init__(*args ,**kwargs)
        self.fields['location'].empty_label ='select your zone'      



class OrderItemForm(forms.ModelForm):

    #product = forms.CharField(max_length=5, required=True, label='product',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    #quantity = forms.IntegerField(max_length=30, required=True,label='quantity',widget=forms.TextInput(attrs={'placeholder': 'first name'}))
    #address = forms.CharField(max_length=30, required=True, label='username',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    #desc = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'placeholder': 'last name'}))
  
    
   
    class Meta:
        model = OrderItem
        fields =('product','quantity','address' ,'description')



#the below class has to be removed

#class CheckoutAddressForm(forms.ModelForm):

   # country = CountryField(blank_label='(select country)').formfield(widgets=CountrySelectWiddgets({
     #   'class':'custom-select d-block w-100' }))
    
   
   # class Meta:
       # model = CheckoutAddress
       # fields="__all__"
        #fields =('product','quantity','address' ,'description')



  

  
        


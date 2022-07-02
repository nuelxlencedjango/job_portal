
from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import *



class ProductForm(forms.ModelForm):
    
    #location =forms.CharField(required=True)
    class Meta:
        model = Product
        #fields = '__all__'
        fields =('name','desc' ,'location')

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
        fields =('product','number_of_workers','description','address')



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
        


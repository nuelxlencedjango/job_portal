from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class CreateUserForm(UserCreationForm):
  username = forms.CharField(max_length=30, required=True, label='username',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
  first_name = forms.CharField(max_length=30, required=True,label='first_name',widget=forms.TextInput(attrs={'placeholder': 'first name'}))
  last_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'placeholder': 'last name'}))
  email = forms.EmailField(max_length=100,required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
  password1 = forms.CharField(max_length=50,required=True ,widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
  password2 = forms.CharField(max_length=50, required=True ,widget=forms.TextInput(attrs={'placeholder': 'Re-enter password'}))
  
  class Meta:
    model = User
    fields =('username','first_name','last_name' ,'email','password1','password2')


  def save(self, commit=True):

    user = super().save(commit=False)  
    user.username =self.cleaned_data['username']
    user.first_name =self.cleaned_data['first_name']
    user.last_name =self.cleaned_data['last_name']
    user.email =self.cleaned_data['email']
    user.password1 =self.cleaned_data['password1']

    if commit:
      user.save()
    return user

    
 
class WorkersForm(ModelForm):
  address = forms.CharField(max_length=200, required=True,label='address',widget=forms.TextInput(attrs={'placeholder': 'address'}))
  phone = forms.CharField(max_length=15, required=True,label='phone',widget=forms.TextInput(attrs={'placeholder': 'phone'}))
  profile_img =CloudinaryField()
  nin = forms.CharField(max_length=15, required=True,label='NIN',widget=forms.TextInput(attrs={'placeholder': 'NIN'}))
  years_experience = forms.CharField(max_length=100, required=True,label='years experience',widget=forms.TextInput(attrs={'placeholder': 'how many years experience?'}))
  class Meta:
    model = Artisan
    fields ="__all__"
  
  
  def __init__(self ,*args ,**kwargs):
    super(WorkersForm ,self).__init__(*args ,**kwargs)
    self.fields['location'].empty_label ='select your zone'  
  

  
class UserUpdateForm(forms.ModelForm):
  username = forms.CharField(max_length=30, required=True, label='username',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
  first_name = forms.CharField(max_length=30, required=True,label='first_name',widget=forms.TextInput(attrs={'placeholder': 'first name'}))
  last_name = forms.CharField(max_length=30, required=True,label='last_name',widget=forms.TextInput(attrs={'placeholder': 'last name'}))
  email = forms.EmailField(max_length=100,required=True,label='email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

  class Meta:
    model = User
    fields =('username','first_name','last_name' ,'email')



class ArtisanUpdateForm(forms.ModelForm):
  address = forms.CharField(max_length=30, required=True,label='address',widget=forms.TextInput(attrs={'placeholder': 'address'}))
  phone = forms.CharField(max_length=15, required=True,label='phone',widget=forms.TextInput(attrs={'placeholder': 'phone'}))
  nin = forms.CharField(max_length=30, required=True,label='nin',widget=forms.TextInput(attrs={'placeholder': 'nin'}))
  years_experience = forms.CharField(max_length=100, required=True,label='years experience',widget=forms.TextInput(attrs={'placeholder': 'how many years experience?'}))
 
  class Meta:
    model =Artisan
    fields =('address','phone','location','nin','years_experience')    



class BankDetailForm(forms.ModelForm):

  class Meta:
    model =BankDetails
    fields =('bank_name','account_number','account_type','account_name') 



class BankUpdateForm(forms.ModelForm):
  class Meta:
    model =BankDetails
    fields =('bank_name','account_number','account_type','account_name') 

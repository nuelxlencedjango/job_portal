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

    


class CustomerForm(forms.ModelForm):
  phone = forms.CharField(max_length=15, required=True,label='phone',widget=forms.TextInput(attrs={'placeholder': 'phone'}))
  
  class Meta:
    model =Customer
    fields = '__all__'







class UserUpdateForm(forms.ModelForm):

  username = forms.CharField(max_length=30, required=True, label='username',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
  first_name = forms.CharField(max_length=30, required=True,label='first_name',widget=forms.TextInput(attrs={'placeholder': 'first name'}))
  last_name = forms.CharField(max_length=30, required=True,label='last_name',widget=forms.TextInput(attrs={'placeholder': 'last name'}))
  email = forms.EmailField(max_length=100,required=True,label='email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

  class Meta:

    model = User
    fields =('username','first_name','last_name' ,'email')



class CustomerUpdateForm(forms.ModelForm):
  phone = forms.CharField(max_length=15, required=True,label='phone',widget=forms.TextInput(attrs={'placeholder': 'phone'}))

  class Meta:
    model =Customer
    fields =('phone',)
    



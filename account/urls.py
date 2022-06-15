from django.urls import path
from .views import *
from .import views

from django.contrib.auth import views as auth_views



app_name = 'account'


urlpatterns = [
     #path('', views.account_product, name='home'),
    path('registration/',views.registration,name ='registration'),
    path('register/',views.registerPage,name ='register'),
    #path('register/',views.registration,name ='register'),
    path('login/' ,views.loginPage , name='login'),
    path('admin_page/',views.adminPage ,name='admin_page'),
    path('update_info/', views.update_info, name="update_info"),
   
    path('logout/', views.logoutPage, name='logout'),
  

  #new info
    path('dashboard/',views.clientDashboard,name ='dashboard'),
    
    path('client_register/',views.clientRegister,name ='client_register'),

    
]

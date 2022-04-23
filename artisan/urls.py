from os import name
from django.urls import path
from .views import *
from .import views

from django.contrib.auth import views as auth_views



app_name = 'artisan'


urlpatterns = [
     path('artisanReg/', views.artisanRegistration, name='artisanReg'),
     path('confirmed_orders/', views.confirmedOrders, name='confirmed_orders'),
     path('artisan_update/', views.artisan_update, name="artisan_update"),
     path('paidJobs',views.paidJobs, name='paidJobs'),
     path('job_detail/<int:id>/',views.jobDetail, name='job_detail'),
     path('services_completed/',views.artisan_services, name='services_completed'),
     path('current_job/', views.currentJob, name='current_job'),
     # path('register_job/', views.registerJob, name='register_job'),

    
]


from django.urls import path
from .views import *
from .import views

app_name = 'products'


urlpatterns = [
    

    path('', views.home, name='home'),
    path('update_order/<int:pk>/',views.updateOrder,name='update_order'),
    path('detail/<int:id>/', views.details, name='detail'),
     path('jobs/' , AvailableJobs.as_view() ,name="jobs"),
    path('terms/',views.terms_and_conditions, name="terms"),
    
    path('product_dest/<pk>', views.product_dest, name='product_dest'),
    path('orderlist/', views.orderlist, name='orderlist'),
    path('add_to_cart/<pk>', views.add_to_cart, name='add_to_cart'),
    path('orderlist/', views.orderlist, name='orderlist'),
    path('add_item/<int:pk>', views.add_to_cart, name='add_item'),
    path('remove_item/<int:pk>', views.delete_order, name='remove_item'),

    path('search/', views.search , name='search'),
    path('contact/',views.contact ,name='contact'),
    
    path('payment/', views.payment, name='payment'),
     path('handle_confirmation/', views.handle, name='handle_confirmation'),
     path("post_service/", views.postServiceNeeded, name="post_service"),


    path('new/', views.newMethod, name='new'),
    path('add_service_item/<int:pk>', views.serviceRequestCart, name='add_service_item'), 
    path('servicelist/', views.Servicelist, name='servicelist'),
    path('service_payment/', views.servicePayment, name='service_payment'),

    path('payment_confirmation/', views.paymentConfirmation, name='payment_confirmation'),

    path("post_job/", views.PostJobItem, name="post_job"),

     path('service_list/', views.Servicelisting, name='service_list'),

    path('train_staff/', views.StaffTraining, name='train_staff'),
    
    path("workers_detail/", views.artisanDetail, name="workers_detail"),
    path("all_services/", views.serviceCompeleted, name="all_services"),
]




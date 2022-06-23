from django.urls import path
from .views import *
from .import views

app_name = 'products'


urlpatterns = [
    
    path('', views.home, name='home'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout ,name='checkout'),
    path('update_order/<int:pk>/',views.updateOrder,name='update_order'),
    
    # remove this update_item
    path('update_item/',views.updateItem,name='update_item'),



    path('detail/<int:id>/', views.details, name='detail'),
     path('jobs/' , AvailableJobs.as_view() ,name="jobs"),
    #path('product_dest/<pk>', ProductDetail.as_view() ,name="product_dest"),

    path('terms/',views.terms_and_conditions, name="terms"),
    path('product_desc/<pk>', views.product_desc, name='product_desc'),

    path('product_dest/<pk>', views.product_dest, name='product_dest'),
    #path('add_to_cart/<pk>', views.add_to_cart, name='add_to_cart'),
    path('orderlist/', views.orderlist, name='orderlist'),
   
    path('product_desc/<pk>', views.product_desc, name='product_desc'),
    path('add_to_cart/<pk>', views.add_to_cart, name='add_to_cart'),
    path('orderlist/', views.orderlist, name='orderlist'),
    path('add_item/<int:pk>', views.add_to_cart, name='add_item'),
    path('remove_item/<int:pk>', views.delete_order, name='remove_item'),

    path('search/', views.search , name='search'),

     #path('flip-searching/', views.flipSearch , name='flip-searching'),

    path('contact/',views.contact ,name='contact'),
    
    path('payment/', views.payment, name='payment'),
    path('payment_confirmation/', views.payment_confirmation, name='payment_confirmation'),

     path('handle_confirmation/', views.handle, name='handle_confirmation'),


   

    path('new/', views.newMethod, name='new'),


    path('add_service_item/<int:pk>', views.serviceRequestCart, name='add_service_item'), 
    path('servicelist/', views.Servicelist, name='servicelist'),
    path('service_payment/', views.servicePayment, name='service_payment'),
]




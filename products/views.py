from os import name
from django.shortcuts import render,redirect ,get_object_or_404, resolve_url
from django.contrib import auth, messages
import json 

from django.utils import timezone

from django.http import HttpResponse,JsonResponse, request
from django.forms import inlineformset_factory
from django.views.generic.base import TemplateView

from django.views.generic import (
    ListView ,DetailView, CreateView, UpdateView ,DeleteView
)
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

#import products                 
from .models import *
from django.db.models import Q 

from django.core.mail import send_mail

from django.conf import settings
from .forms import *

# to be removed
#razorpay_client = razorpay.Client(auth=(settings.razorpay_id, settings.razorpay_screet))

# Create your views here.

# heroku ps:scale web=1 
#heroku buildpacks:clear
#git commit --allow-empty -m "Adjust buildpacks on Heroku
#
# git push heroku main

def home(request):
    #prod = Product.objects.all()
    products = Production.objects.all()
    prod = Product.objects.all()
    context ={
        'products':products,'prod':prod
    }

    #return render(request ,'products/items.html',context)
    return render(request,'homePage.html',context)



class HomeView(ListView):
    model = Product
    template_name = 'home.html'




def cart(request):
    if request.user.is_authenticated:
        customer = request.user.details.customer
        order, created = Orders.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_item':0, 'shipping':False} 
        cartItems = order['get_cart_items']


    context = {'items':items, 'order':order, 'cartItems':cartItems } 
    return render(request, 'products/orderlist.html', context)


def checkout(request):
    if request.is_authenticated:
        customer = request.user.details.customer

        order, created = Orders.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    
    else:
        items = []
        ordering = {'get_cart_total':0 , 'get_cart_item':0}  

   

    context = {'items':items, 'order':order } 
    return render(request, 'products/checkout.html', context)        

  
  

def updateOrder(request,pk):
    order = OrderItem.objects.get(pk=pk)
    form = OrderItemForm(instance = order)
    if request.method =="POST":
        form =OrderItemForm(request.POST,instance =order)
        if form.is_valid():
            form.save()
            message = "Successfully updated your item"
            return redirect('products:orderlist')
           
        else:
            message = "Not successful.Pls retry!"   

    context = {'form':form}

    return render(request,'products/update_order.html',context)         


def delete_order(request,pk):
    item = OrderItem.objects.get(pk=pk)
    item.delete()
    return redirect('products:orderlist')  




def updateItem(request):
    data = json.loads(request.body)
    productId =data['productId']
    action = data['action']
    #print('action:',action, 'productId :','\n', productId)

    customer = request.user
    product = Production.objects.get(id= productId)
    #order,created = Order.objects.get_or_create(customer=customer,complete=False)
    order,created = Orders.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItems.objects.get_or_create(orders=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1) 
        return render(request, 'product/orderlist')
        message = "Added"

    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        message = "Removed"

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete() 
        message = "Deleted"
        #return redirect("ecom:orderlist")   

    
    ctx = {'message': message}


    #return JsonResponse('item was added ',safe=False)
    #return render(request, 'product/orderlist',context)
    return HttpResponse(json.dumps(ctx),content_type='application/json')
   

def details(request,id):
    home = Production.objects.get(id=id)
    #out = OutdoorJobs.objects.filter(id=id)
    context ={'home':home,}
               #'out': out }
    return render(request ,'detail.html',context )




class AvailableJobs(TemplateView):
   
    template_name = 'services.html'  


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['jobs'] =Production.objects.all()
        context['prod'] =Product.objects.all()
        return context



        

def product_desc(request, pk):
    desc = Production.objects.get(pk =pk)
    #prod = Product.objects.get(pk=pk)   
    context ={'desc':desc}
    return render(request ,'products/desc.html',context)   
    





def add_to_cart(request, pk):
    if request.user.is_authenticated:

   
        product = Product.objects.get(pk=pk)  
    
        order_item,created = OrderItem.objects.get_or_create(
            product =product,
            user = request.user,
            ordered = False,
            description = request.POST['description'],
        #desc = request.POST.get('desc', False),
            address = request.POST['address'],
        #address = request.POST.get('address', False),
            quantity = int(request.POST['quantity']),

            )
        order_qs = Order.objects.filter(user=request.user,ordered=False)
        if order_qs.exists():
            order =order_qs[0]
            if order.items.filter(product__pk=pk).exists():
                order_item.quantity +=1

                order_item.save()
                messages.info(request ,"Added additional worker successfully")
                return redirect("products:orderlist")

            else:
                order.items.add(order_item)
                messages.info(request ," successfully booked")
                return redirect("products:orderlist")  

        else:
            ordered_date =timezone.now()
            order =Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            messages.info(request," Successfully booked")

            return redirect('products:orderlist')          
    
    else:
        messages.info(request,"Request unsuccessful! Please login before you can make a request")
        return render(request ,'account/service_request.html')   
        




def orderlist(request):
    if Order.objects.filter(user=request.user, ordered =False).exists():
        order = Order.objects.get(user=request.user, ordered=False)
        context={
            'order':order
        }
        return render(request, 'products/orderlist.html',context)

    return render(request ,'products/orderlist.html',{'message': "your cart is empty"})   




def products(request):
    prod = Product.objects.all()
    context ={
        'prod':prod
    }

    return render(request ,'products/items.html',context)
    #return render(request,'index.html',context)




def product_dest(request, pk):
    #desc = Production.objects.get(pk =pk)
    prod = Product.objects.get(pk=pk)   
    context ={'prod':prod}
    return render(request ,'products/dest.html',context) 



def search(request):
    query = request.GET.get('search')
    item = Product.objects.filter(Q(name__icontains =query))

    context ={'item':item}
    if item:
        return render(request,'search.html',context)

    else:
        messages.warning(request,'Service not available at this time')
        return render(request,'search.html',context)
            



def contact(request):
    if request.method =='POST':
        message_name = request.POST['message-name']
        message_phone = request.POST.get("message-phone" ,False)
        message_email = request.POST['message-email']
        message  = request.POST['message']

        # seend a mail
        send_mail(
            message_name , # email subject
            message ,      # main message
            message_email , # from email 
            [settings.EMAIL_HOST_USER], # recipient, to email
        fail_silently=False)
        
        
        #contacts = ContactUs(name=message_name ,phone=message_phone ,email=message_email ,message=message)
        contacts = ContactUs()
        contacts.name =message_name
        contacts.phone = message_phone
        contacts.email = message_email
        contacts.message = message
        contacts.save()


        return render(request ,'contact.html',{'message_name' :message_name}) 

    else:
        return render(request ,'contact.html' ,{}) 



def payment(request):
    if Order.objects.filter(user=request.user, ordered =False).exists():

        order = Order.objects.get(user=request.user, ordered=False)
        context ={'order':order}
        return render(request, 'payments/payment.html',context) 

    return render(request ,'products/orderlist.html',{'message': "your cart is empty"})            


#should be removed
#def checkout_page(request):
    #if CheckoutAddress.objects.filter(user=request.user).exists():
    #    return render(request,'checkout.html',{'payment_allow':'allow'})

   # if request.method =="POST":
     #   form =CheckoutAddressForm(request.POST)

      #  try:
         #   if form.is_valid():
              #  street_address = form.cleaned_data.get('street_address') 
              #  apartment_address = form.cleaned_data.get('apartment_address') 
              #  country = form.cleaned_data.get('country') 
               # zip_code = form.cleaned_data.get('zip')    

               # checkout_address = CheckoutAddress(
                #    user =request.user,
                #    street_address = street_address,
                #    apartment_address =apartment_address,
                #    country = country,
                 #   zip_code = zip_code
               # )
               # checkout_address.save()

               # return render(request,'checkout.html',{'payment_allow':'allow'})

        #except Exception as e:
          #  context={'e':e}
           # messages.warning(request,'failed checkout',context)
           # return redirect('product:orderlist')

    #else:
        #form = CheckoutAddressForm()    
        #return render(request,'checkout.html',{"form":form})    


@csrf_exempt
def payment_confirm(request):
    try:

        order = Order.objects.get(user=request.user, ordered=False)
        order_amount = order.get_total_price()
        order_currency = "NGA"
        order_receipt = order.order_id
        note ={"stree_address":address.street_address,
           "aprtment_address":address.apartment_address,
           "country":address.country.name,
           "zip_code":address.zip_code }
        razorpay_order = razorpay_client.order.create(
         dict(
             amount=order_amount ,
             currency =order_currency,
             receipt =order_receipt,
             notes= notes,
             payment_capture ="0"
         )
     )
        print(razorpay_order["id"])
        order.razorpay_order_id = razorpay_order["id"]
        order.save()

        context ={
        "order":order,
        "order_id":razorpay_order["id"],
        "orderId":order.order_id,
        "final_price":order_amount,
        "razorpay_merchant_id":settings.razorpay_id
        }
        return render(request,"pay.html",context) 


    except Order.DoesNotExist:
        return HttpResponse("404 error")


@csrf_exempt
def payment_confirmation(request):
    order = Order.objects.get(user=request.user, ordered=False)
    id = order.id
    if id:
        context ={'id':id}

        return redirect('product:handle_confirmation')

    

    return render(request,"payments/unsuccessful.html")
    #paid_services =Order.objects.get(user=request.user, ordered=True,order_id =payment_id)
    #context ={"paid_services":paid_services}
        #except:
            #return HttpResponse("error occurred")  
            
             

def handle_confirmation(request):
    if Order.objects.filter(user=request.user, ordered =True).exists():
        #if OrderItem.objects.filter(user=request.user, ordered=True).exists():

        paid_services = Order.objects.filter(user=request.user, ordered=True)
        context ={'paid_services':paid_services}
        return render(request, 'payments/payment_confirmation.html',context) 
        

        #return render(request ,'payments/pay.html') 

    return render(request ,'payments/no_order.html')             




@csrf_exempt
def handlerequest(request):
    if request.method == "POST":
        try:
            payment_id =request.POST.get("razorpay_payment_id")
            order_id =request.POST.get("razorpay_order_id")
            signature =request.POST.get("signature")

            params_dict ={
                "razorpay_order_id":order_id,
                "razorpay_payment_id":payment_id,
                "razorpay_signature":signature
            }
            try:
                order_db = Order.objects.get(razorpay_order_id=order_id)
            except:
                return HttpResponse("505 not found")  

            order_db.razorpay_payment_id =payment_id
            order_db.razorpay_signature =signature
            order_db.save()
            result =razorpay_client.utility.verify_payment_signature(params_dict)
            if result == None:
                amount =order_db.get_total_price()  
                amout = amount *100
                payment_status =razorpay_client.payment.captur(payment_id,amount)
                if payment_status is not None:
                    order_db.ordered = True
                    order_db.save()   
                    

                    order_db.ordered = False
                    order_db.save()
                    request.session["order_failed"]   = "unfortunately your order could not be placed"

                    return redirect("/")
                else:
                    order_db.ordered =False
                    order_db.save()
                    return render(request, "paymentfail.html") 
        except:
            return HttpResponse("error occurred")             
    #Order.save()

        #context = {'order':order}
        #if order:
            #order.ordered=True
            #order.save()
       
            #    mes = "there are orders"
           # else:
             #   mes ="wrong logic"    
                #confirmed_order  = Order.objects.get(user=request.user, ordered=True)

                #context ={'confirmed_order ':confirmed_order }

                #messages.info(request ,"Payment was successfully")
            #return render(request,'payments/payment_confirmation.html')

    #return render(request,'payments/pay.html',{'nothing':'nothig'})    

def cartContent(request):
    if request.user.is_authenticated():
        customer = request.user.customer
        order,created = Order.objects.get_or_create(user=customer, ordered =False)
        items = Order.orderitem_set.all()
  

def add_to_shop(request,pk):
    product = get_object_or_404(Product,pk=pk)

    order_item,created =OrderItem.objects.get_or_create(
        product=product,
         #description = request.POST.get('description'),
          #address = request.POST.get('address'),
          #quantity = request.POST.get('quantity')
    )

    order_qs = Order.objects.filter(user =request.user, ordered=False)

    if order_qs.exists():
        order =order_qs[0]

        if order.items.filter(product__pk=product.pk).exists():
            order_item.quantity +=1
            order_item.save()

            messages.info(request ,"Added additional worker successfully")
            return redirect("product:orderlist")


    else:
        ordered_date =timezone.now()
        order = Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)

        messages.info(request," Successfully booked")
        return redirect('product:orderlist')






def terms_and_conditions(request):
    return render(request,'terms_and_conditions.html')      


         
   
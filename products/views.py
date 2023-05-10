
from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib import auth, messages
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView 
)
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from account.models import Customer                
from .models import *
from django.db.models import Q 
from django.core.mail import send_mail
from django.conf import settings
from .forms import *

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

#8162810489


def home(request): 
    prod = Product.objects.all()
    context ={'prod':prod }

    return render(request,'homePage.html',context)



#list of jobs available
class AvailableJobs(TemplateView):
    template_name = 'services.html'  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['service'] = Services.objects.all()
        context['prod'] =Product.objects.all()
        return context

    
#updating order
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



def details(request,id):
    home = Product.objects.get(id=id)
    context ={'home':home,}
             
    return render(request ,'detail.html',context )
 
    

def add_to_cart(request, pk):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=pk)  
    
        order_item,created = OrderItem.objects.get_or_create(
            product =product,
            user = request.user,
            ordered = False,
            description = request.POST['description'],
       
            address = request.POST['address'],
            quantity = int(request.POST['quantity']),)

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
 




def product_dest(request, pk):
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

        send_mail(
            message_name , # email subject
            message ,      # main message
            message_email , # from email 
            [settings.EMAIL_HOST_USER], # recipient, to email
        fail_silently=False)
        
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




@csrf_exempt
def payment_confirmation(request):
 
    order = Order.objects.get(user=request.user, ordered=False)
    #get payment receipt from flutter wave
    payment_id =request.POST.get("tx_ref")
    
    order = Order.objects.get(user=request.user, payment_id=payment_id,ordered=False) 
    order.ordered = True
    order.save()
    if OrderItem.objects.filter(user=request.user, ordered=False,status='Pending'):
        OrderItem.objects.filter(user=request.user, ordered=False,status='Pending').update(ordered=True,status='Paid')

        if OrderItem.objects.filter(user=request.user, ordered=True,status='Paid'):
           
            return redirect('products:handle_confirmation')

        else:
            return render(request,'payments/no_order.html')    
       
        
    return redirect('products:home')

       
  
            
             

def handle_confirmation(request):
    if Order.objects.filter(user=request.user, ordered =True).exists():

        order_list = Order.objects.filter(user=request.user, ordered=True)   
        context ={'order_list':order_list}

        return render(request, 'payments/payment_confirmation.html',context) 
        
    return render(request ,'payments/no_order.html')             



def handle(request):

    list_items = ServiceOrder.objects.filter(user=request.user,ordered=True).order_by('-datetime_ofpayment')

    context ={'list_items':list_items}
    return render(request, 'payments/payment_details.html',context) 
   
        
    
    
  

def add_to_shop(request,pk):
    product = get_object_or_404(Product,pk=pk)

    order_item,created =OrderItem.objects.get_or_create(
        product=product,
       
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






class HomeView(ListView):
    model = Product
    template_name = 'new/home.html'

    def get_queryset(self, *args,**kwargs):
        qs= super(HomeView, self).get_queryset(*args, **kwargs)
        qs = qs.ordered_by('-date_added')


#new method


def newMethod(request):

    prod = Product.objects.all()
    address = OurLocations.objects.all()
    context ={
        'address':address,
        'prod':prod,
       
    }
    return render(request,'new/home.html',context)  





def serviceRequestCart(request, pk):
    if request.user.is_authenticated:

        artisan = Artisan.objects.get(pk=pk)  
        artisan_name = artisan.user.last_name
        job = artisan.profession_name 
        item = Product.objects.get(name=job)
    
        service_item,created = ServiceRequest.objects.get_or_create(
            artisan =Artisan.objects.get(pk=pk), #artisan,
            product =item,
            user = request.user,
            ordered = False,
            description = request.POST['description'],
            address = request.POST['address'],
            number_of_workers = int(request.POST['number_of_workers']),
           

        )
        order_qs = ServiceOrder.objects.filter(user=request.user,ordered=False)
        if order_qs.exists():
            order =order_qs[0]
            if order.items.filter(product__pk=pk).exists():
                service_item.number_of_workers +=1

                service_item.save()
                messages.info(request ,"Added additional worker successfully")
                return redirect("products:servicelist")

            else:
                order.items.add(service_item)
                messages.info(request ," successfully booked")
                return redirect("products:servicelist")  

        else:
            ordered_date =timezone.now()
            order =ServiceOrder.objects.create(user=request.user, ordered_date=ordered_date)
            order.items.add(service_item)
            messages.info(request," Successfully booked")

            return redirect('products:servicelist')          
    
    else:
        messages.info(request,"Request unsuccessful! Please login before you can make a request")
        return render(request ,'account/service_request.html')              
        





#client unpaid request list
def Servicelist(request):
    if ServiceOrder.objects.filter(user=request.user, ordered =False).exists(): #or PostJob.objects.filter(user=request.user, paid =False).exists():
        order = ServiceOrder.objects.get(user=request.user, ordered=False)
        context={
            'order':order,'listing': 'listing'
        }
     
        return render(request, 'dashboard/client/clients.html',context) 
    return render(request ,'dashboard/client/clients.html',{'message': "your cart is empty"})   




def servicePayment(request):
    if ServiceOrder.objects.filter(user=request.user, ordered =False).exists():

        order = ServiceOrder.objects.get(user=request.user, ordered=False)
        context ={'order':order}
        return render(request, 'payments/payment.html',context) 

    return render(request ,'products/serviclist.html',{'message': "your cart is empty"}) 







@csrf_exempt
def paymentConfirmation(request):
 
    order = ServiceOrder.objects.get(user=request.user, ordered=False)
    #get payment receipt from flutter wave
    payment_id =request.POST.get("tx_ref")
    
    order = ServiceOrder.objects.get(user=request.user, payment_id=payment_id,ordered=False) 
    order.ordered = True
    order.save()

    #orderItem goods
    if ServiceRequest.objects.filter(user=request.user, ordered=False,status='Pending'):
        #updating status when payment is confirmed
        ServiceRequest.objects.filter(user=request.user, ordered=False,status='Pending').update(ordered=True,status='Paid')

        if ServiceRequest.objects.filter(user=request.user, ordered=True,status='Paid'):
           
            return redirect('products:handle_confirmation')

        else:
            return render(request,'payments/no_order.html')    
       
    return redirect('products:home')


#list of services
def ourServices(request):
    service = Services.objects.all()

    context ={'service':service}
    return render(request,'services.html' , context) 


#client posting the job he wants
@login_required(login_url='/account/login')
def PostJobItem(request):

    form = PostJobForm()
    if request.method == 'POST':
        
        form = PostJobForm(request.POST)
        if form.is_valid():
                job_obj = form.save(commit=False)
                job_obj.user = request.user
                job_obj.save()
                return redirect('account:dashboard')
                
    context={'form': form}
    return render(request, 'post/post_job.html', context)



#
@login_required(login_url='/account/login')
def postServiceNeeded(request):
    form = PostServiceForm()
    if request.user.is_authenticated and Customer.objects.filter(user=request.user):
        if request.method == 'POST':

            form = PostServiceForm(request.POST)
          
            if form.is_valid():
                job_obj = form.save(commit=False)
    
                order_item,created = ServiceRequest.objects.get_or_create(
                product = job_obj.product,
                user = request.user,
                ordered = False,
                description = job_obj.description,
                address =job_obj.address,
                number_of_workers = job_obj.number_of_workers,
                location =job_obj.location,

            )
            order_qs = ServiceOrder.objects.filter(user=request.user,ordered=False)
            if order_qs.exists():
                order =order_qs[0]
                if order.items.filter(product__name=order_item.product).exists():
                    order_item.number_of_workers +=1

                    order_item.save()
                    messages.info(request ,"Added additional worker successfully")
                    return redirect("account:dashboard")

                else:
                    order.items.add(order_item)
                    messages.info(request ," successfully booked")
                    return redirect("account:dashboard")  

            else:
                ordered_date =timezone.now()
                order =ServiceOrder.objects.create(user=request.user, ordered_date=ordered_date)
                order.items.add(order_item)
                messages.info(request," Successfully booked")

                return redirect('account:dashboard')          
    
        else:
            messages.info(request,"Request unsuccessful! Please login as before you can make a request")
           
            context={'form':form}
            return render(request, 'post/post_job.html',context) 

    messages.info(request," Please login as a client before you can make a request")    
    return render(request, 'artisans/as_client.html') 




def Servicelisting(request):
    serv= ServiceOrder.objects.filter(user=request.user, ordered =False)
    post = PostJob.objects.filter(user=request.user, paid=False)

    if serv or post:
        
        context={
            'serv':serv,'post':post,'listing':'listing',
        }
        return render(request, 'dashboard/client/clients.html',context)

    return render(request ,'dashboard/client.html',{'message': "your cart is empty"}) 





@login_required(login_url='/account/login')
def StaffTraining(request):

    form = TrainingStaff()
    if request.method == 'POST':

        form = TrainingStaff(request.POST)
        if form.is_valid():
                job_obj = form.save(commit=False)
                job_obj.user = request.user
                job_obj.save()
                return redirect('account:dashboard')
                
    context={'form': form}
    return render(request, 'post/staff_training.html', context)    



#artisan details
def artisanDetail(request):
    if ServiceRequest.objects.filter(user=request.user,ordered=True,status="Paid",accepted="Accepted").exists():
        artisans_info=ServiceRequest.objects.filter(user=request.user,ordered=True,status="Paid",accepted="Accepted").order_by('-date_created')
        context ={'artisans':artisans_info}
        return render(request,'dashboard/client/artisan_info.html',context)
           
    elif ServiceRequest.objects.filter(user=request.user,ordered=True,status="Paid").exists():
        messages.info(request,"The artisan is preparing to take up the job")
           
        return render(request,'dashboard/client/artisan_info.html')

    elif ServiceRequest.objects.filter(user=request.user,ordered=False,status="No").exists():  
        messages.info(request,"KIndly make payment to confirm your request") 
        return render(request,'dashboard/client/artisan_info.html')  


    else:     
        messages.info(request,"You dont have any request yet")
        return render(request,'dashboard/client/artisan_info.html')
  

    
#services completed 
def serviceCompeleted(request):
    if ServiceRequest.objects.filter(user=request.user,ordered=True,status="Paid",accepted="Accepted",work_done=True).exists():
        all_jobs=ServiceRequest.objects.filter(user=request.user,ordered=True,status="Paid",accepted="Accepted",work_done=True).order_by('-date_created')
        context ={'all_jobs':all_jobs}
        return render(request,'dashboard/client/completed_services.html',context)

    else:
        messages.info(request," Either you dont have any request yet or your job is still in progress")    
        return render(request,'dashboard/client/completed_services.html')
           
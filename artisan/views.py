from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
#from django.http import HttpResponse
#from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
#from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import Group
from products .models import *
from django.db.models import Q 


#from .filters import OrderFilter
from .models import *
from .forms import *


# Create your views here.

def artisanRegistration(request):
    if request.method == 'POST':
        form1 = CreateUserForm(request.POST)
        form4 = WorkersForm(request.POST,request.FILES) 

        if form1.is_valid() and form4.is_valid():
            user = form1.save()
            profile = form4.save(commit=False)
            profile.user =user
            profile.save()
            img_obj = form4.instance

            id = form1.cleaned_data.get('id')

            messages.success(request, 'Account was created for ' , id)

            return redirect('account:login')


       
    else:
        form1 =CreateUserForm()
        form4 = WorkersForm()
        #form3 = ArtisanForm()
        
        
        
    context = {'form1':form1, 'form4': form4}   
    return render(request, 'account/artisan_register.html', context)


#def availableJob(request):
 #   return render(request, 'available_order.html')



def confirmedOrders(request):
    return render(request ,'artisans/available_jobs.html')  




def artisan_update(request):
    if request.method =="POST":

        form1 = UserUpdateForm(request.POST, instance = request.user)
        form4 = ArtisanUpdateForm(request.POST, request.FILES,instance = request.user.artisan)

        if form1.is_valid() and form4.is_valid():
            form1.save()
            form4.save()

            messages.success(request,"Successfully updated")
            return redirect('artisan:confirmed_orders')
               
        else:
            messages.warning(request,"Not updated")
    
    else:
        form1 = UserUpdateForm(instance = request.user)
        form4 = ArtisanUpdateForm(instance=request.user.artisan)          

    context = {'form1':form1, 'form4':form4}

    return render(request,'account/update_artisan_info.html',context)  






def paidJobs(request):
    artisan = Artisan.objects.filter(user=request.user)
    
    job_location = request.user.artisan.location
    job_address = request.user.artisan.address

#to be changed to orderitem.objects.filter
    services_paid_for = Order.objects.filter(ordered =True)
    #services_paid_for = OrderItem.objects.filter(ordered =True,status='Paid')

    areaJobs = OrderItem.objects.filter(Q(address__icontains=job_location) | Q(address__icontains=job_address) )

    context ={'services_paid_for':services_paid_for,'artisan':artisan,'areaJobs':areaJobs}


    
    return render(request,'products/paid_services.html',context)


def jobDetail(request,id):
   # limit = 0
    artisan = [Artisan.objects.filter(user=request.user)]

    job_info= OrderItem.objects.filter(id =id)
    for a in job_info:
        name = a.product.name



    #work here -conditions
    #job_info.artisan_assigned.set(artisan)



    context = {'job_info': job_info,'name':name }
    return render(request,'products/job_detail.html',context)



def currentJob(request):
    user = Artisan.objects.get(user=request.user)

    #job = OrderItem.objects.all()
    if OrderItem.objects.filter(artisan_assigned=user).exists():
        current_job = OrderItem.objects.filter(artisan_assigned=user)[0]

        context ={'current_job':current_job}
    return render(request,'artisans/current_job.html',context)




def artisan_services(request):
    user = Artisan.objects.get(user=request.user)

    #job = OrderItem.objects.all()
    if OrderItem.objects.filter(artisan_assigned=user).exists():
        job_info = OrderItem.objects.filter(artisan_assigned=user).order_by('-date_created')
        context ={'job_info':job_info}
    return render(request,'artisans/completed_services.html',context)
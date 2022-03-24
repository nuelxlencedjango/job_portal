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
        form4 = WorkersForm(request.POST) 

        if form1.is_valid() and form4.is_valid():
            user = form1.save()
            profile = form4.save(commit=False)
            profile.user =user
            profile.save()

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
    
    phone = request.user.artisan.location
    area = request.user.artisan.address

    services_paid_for = Order.objects.filter(ordered =True)

    areaJobs = Order.objects.filter(Q(location__icontains=area) | Q(address__icontains=phone) )

    #context ={'services_paid_for':services_paid_for,'artisan':artisan,'phone':areaJobs}
   

    context ={'services_paid_for':services_paid_for,'artisan':artisan,'phone':phone ,'area':area}

    return render(request,'products/paid_services.html',context)
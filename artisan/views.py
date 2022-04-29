from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
#from django.http import HttpResponse
#from django.forms import inlineformset_factory
from django.http import Http404
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



@login_required
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





@login_required
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



@login_required
def jobDetail(request,id):

    if request.user.is_authenticated:
        artisan = [Artisan.objects.filter(user=request.user)]
        job_info= OrderItem.objects.filter(id =id)
        
        for job in job_info:
            pn =job.id
            job_detail,create =ViewedJob.objects.get_or_create(user=request.user,
            job_name=job.product.name,category=job.product.category,
            description =job.description,price =job.get_service_rate(),client=job.user.last_name,address =job.address,
            date=job.date_created,phone=job.user.details.phone
        )
  
    context = {'job_info': job_info,'pt':pn }
    return render(request,'products/job_detail.html',context)





   #if request.user.is_authenticated:

      #  artisan = [Artisan.objects.filter(user=request.user)]

      #  if OrderItem.objects.filter(id =id).exists():
       #     job_info= OrderItem.objects.filter(id =id)
         #   for job in job_info:
          #      for name in job.artisan_assigned.all():
          #          name.artisan_assigned.set(artisan)
                    
                    #name.update()



@login_required  
def jobAccepted(request,id):
    artisan = [Artisan.objects.get(user=request.user)]
 
    if OrderItem.objects.get(id=id, ordered=True,status='Paid'):

        accepted_job= OrderItem.objects.filter(id=id, ordered=True,status='Paid')
        for b in accepted_job:
            b.artisan_assigned.set(artisan)
            #b.save()
        OrderItem.objects.filter(id=id, ordered=True,status='Paid').update(accepted ="Accepted" ,
        accepted_date =timezone.now())
         
    
     
    if ViewedJob.objects.filter(user=request.user).exists():

        current_job = ViewedJob.objects.filter(user=request.user).last()
        ViewedJob.objects.filter(user=request.user).update(accepted ="Accepted" ,
        accepted_date =timezone.now())

       
        return redirect('artisan:confirmed_orders')
        

    return redirect('/')
                       
                    
  




def currentJob(request):
    user=request.user  
    if ViewedJob.objects.filter(user=user,accepted='Accepted',completed='completed').exists():
        messages.info(request,'You have already confirmed that you are through with the job.')
        return redirect('artisan:confirmed_orders')

    elif ViewedJob.objects.filter(user=user,accepted='Accepted').exists():
       
        current_job = ViewedJob.objects.filter(user=user).last()


        context ={'current_job':current_job}
    return render(request,'artisans/current_job.html',context)





def CurrentJobInfo(request):
    user = request.user

    if ViewedJob.objects.filter(user=user,accepted='Accepted',completed='completed').exists():
        messages.info(request,'You confirmed that you are through with the job.Please contact the admin')
        return redirect('artisan:confirmed_orders')

    elif ViewedJob.objects.filter(user=user,accepted='Accepted').exists():
        try:

            jobinfo = ViewedJob.objects.filter(user=user).last()
    
        except:
            raise Http404
        return render(request, 'artisans/currentjobinfo.html', {'jobinfo':jobinfo})

    




def completeJob(request,id):
    user = request.user
    if ViewedJob.objects.filter(user=user,accepted='Accepted').exists():

        ViewedJob.objects.filter(id=id,user=user,accepted='Accepted').update(completed='Compeleted')
    
    
    messages.info(request,'Congratualtions!You will receive your payment soon')
    return redirect('artisan:confirmed_orders')






def artisan_services(request):
    user = Artisan.objects.get(user=request.user)

    #job = OrderItem.objects.all()
    if OrderItem.objects.filter(artisan_assigned=user,accepted='Accepted',completed='completed').exists():

        job_info = OrderItem.objects.filter(artisan_assigned=user).order_by('-date_created')
        
    context ={'job_info':job_info}
    return render(request,'artisans/completed_services.html',context)
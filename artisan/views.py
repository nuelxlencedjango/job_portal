from multiprocessing import context
from urllib import request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
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

  
def jobAccepted(request,id):
    artisan = [Artisan.objects.filter(user=request.user)]
    #job_info= OrderItem.objects.filter(id =id)
    #id = job_info.id
    if OrderItem.objects.filter(id =id).exists():
        job_info= OrderItem.objects.filter(id =id)
        for job in job_info:
            id = job.id
            #for assignee in job.artisan_assigned.all():
            #for assignee in job_info.artisan_assigned.all():
            for jab in job.artisan_assigned.all():
                name = jab.assignee.user.username
                name.save()
            
            #nin = job.artisan_assigned.nin
            #location=job.artisan_assigned.location
            #hone = job.artisan_assigned.phone
            #profession_name =job.artisan_assigned.profeesional_name
                #name=OrderItem.objects.filter(id =id,artisan_assigned=artisan).update()

                #name.artisan_assigned =artisan
                #name.save()
                context ={'name':name}#,'nin':nin,'location':location,'phone':phone,'profession':profession_name,'assigned':assignee}        
                return render(request,'artisans/accepted_job.html',context)       


    context={'id':id,'nothing found':'nothing'}
    return render(request,'artisans/accepted_job.html',context)               
                    
            #job.artisan_assigned.set(artisan) #=job_info.artisan_assigned.user.username
        #job_info.update()

       
       # for job in job_info:
        #    job_detail,create =ViewedJob.objects.get_or_create(user=request.user,
        #    job_name=job.product.name,category=job.product.category,
        #    description =job.description,price =job.get_service_rate(),client=job.user.last_name,address =job.address,
        #    date=job.date_created,phone=job.user.details.phone
       # )
    #OrderItem.objects.get(id =id)
    #OrderItem.objects.get(id =id)

    #info = OrderItem.objects.filter(id=id)  
  
        #artisan_assigned =assigned.artisan_assigned

        #OrderItem.objects.get(artisan_assigned=job.artisan_assigned.artisan.username).update()

        #job.artisan_assigned=job.user.username
        #job.save()
        #info.update()
        #for name in job.artisan_assigned.all():
            #artisan_assigned=name.user.username
            #artisan_assigned.save()
            #artisan.artisan_assigned.set(artisan)

      
    #info.artisan_assigned.set(request.user.id)  
     
    #job_info= OrderItem.objects.get(id =id)
    #job_info.artisan_assigned.set(artisan)
    
    #for complete in job_detail:
     #   job_complete,create =CompletedJob.objects.get_or_create(user=request.user,
      #      job_name=complete.job_name,category=complete.category,
       #     description =complete.description,pay =complete.price,client=complete.client,address =complete.address,
        #    date=complete.date_created
        #)
   
    #return redirect('artisan:confirmed_orders')   
    
  

def currentJob(request):
    user = Artisan.objects.get(user=request.user)

    #job = OrderItem.objects.all()
    if ViewedJob.objects.filter(user=user).exists():
        current_job = ViewedJob.objects.filter(user=user)[0]

        context ={'current_job':current_job}
    return render(request,'artisans/current_job.html',context)




def artisan_services(request):
    user = Artisan.objects.get(user=request.user)

    #job = OrderItem.objects.all()
    if OrderItem.objects.filter(artisan_assigned=user).exists():
        job_info = OrderItem.objects.filter(artisan_assigned=user).order_by('-date_created')
        context ={'job_info':job_info}
    return render(request,'artisans/completed_services.html',context)
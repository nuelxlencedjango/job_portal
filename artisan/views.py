from itertools import product
from multiprocessing import context
from unittest import result
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

from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView ,DetailView, CreateView, UpdateView ,DeleteView
)

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
       
         
    context = {'form1':form1, 'form4': form4}   
    return render(request, 'account/artisan_register.html', context)


#



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
            return redirect('account:artisanPage')
               
        else:
            messages.warning(request,"Not updated")
    
    else:
        form1 = UserUpdateForm(instance = request.user)
        form4 = ArtisanUpdateForm(instance=request.user.artisan)          

    context = {'form1':form1, 'form4':form4}

    return render(request,'account/update_artisan_info.html',context)  



   #ordered = models.BooleanField(default=False)
   #product = models.ForeignKey(Product, on_delete=models.CASCADE)
 
  
   #status = models.CharField(max_length=200, null=True, blank=True, default='Pending')
  
   #address = models.CharField(max_length=300, null=True,blank=True)
   #artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE,null=True,blank=True)
   #location = models.ForeignKey('artisan.Area' ,on_delete =models.CASCADE ,null=True,blank=True)


#is it all the jobs in the area or based on the service the artisan offers?
@login_required
def paidJobs(request):
    artisan = Artisan.objects.filter(user=request.user)
   
    job_location = request.user.artisan.location
    #job_address = request.user.artisan.address
    job_name   = request.user.artisan.profession_name
    #job_id = artisan.profession_name

    if ServiceRequest.objects.filter(ordered=True,status='Paid',artisan=artisan[0]).exists():
        res=ServiceRequest.objects.filter(ordered=True,status='Paid',artisan=artisan[0])

        if ServiceRequest.objects.filter(ordered=True,status='Paid',artisan=artisan[0],accepted='Accepted').exists():
            messages.info(request ,"No new jobs avaialable now.")
            return render(request,'dashboard/artisan/artisans.html')


        context ={'areaJobs':res}
        return render(request,'dashboard/artisan/artisans.html',context) 


    elif ServiceRequest.objects.filter(ordered=True,status='Paid',product=job_name).exists():        
        res =ServiceRequest.objects.filter(ordered=True,status='Paid',product=job_name)

        context ={'areaJobs':res}
        return render(request,'dashboard/artisan/artisans.html',context) 


    else:
        return redirect('/')   




   

       


    #if ServiceRequest.objects.filter(product=product,ordered =True,status='Paid'):
        #result =ServiceRequest.objects.filter(artisan=Artisan.objects.filter(user=request.user),ordered =True,status='Paid')

     

    #if ServiceOrder.objects.filter(items=job_name,ordered=True):
     #   pass

    #products = ServiceOrder.objects.all()
   
    #for name in products:
        #for item in name.items.all():
            #itt=item.product.id
            #if ServiceOrder.objects.filter(items=itt, ordered =True).exists():
              
                #if ServiceRequest.objects.filter(Q(address__icontains=job_location) | Q(address__icontains=job_address)):
                    #if ServiceRequest.objects.filter(Q(product__name__icontains=job_name)):

                        #areaJobs=ServiceRequest.objects.filter(Q(product__name__icontains=job_name))
            #areaJobs = ServiceRequest.objects.filter(Q(address__icontains=job_location) | Q(address__icontains=job_address) | Q(product__name__icontains=job_name))

                    #context ={'areaJobs':areaJobs}
                    #return render(request,'dashboard/artisan/artisans.html',context) 
                 
            #return render(request,'dashboard/artisan/artisans.html')  
        
         
    #return render(request,'dashboard/artisan/artisans.html')     

               
           
                


         
             
       

   
 
  
		


					             
   



@login_required
def jobDetail(request,id):

    if request.user.is_authenticated:
        artisan = [Artisan.objects.filter(user=request.user)]
        job_info= ServiceRequest.objects.filter(id =id)
        #job_info= OrderItem.objects.filter(id =id)
        #if not ViewedJob.objects.get(job_order_id =id)
        for job in job_info:
            pn =job.id
            
            job_detail,create =ViewedJob.objects.get_or_create(user=request.user,
            job_name=job.product.name,category=job.product.category,
            description =job.description,price =job.get_service_rate(),client=job.user.last_name,address =job.address,
            date=job.date_created,phone=job.user.details.phone,job_order_id=job.id
        )
  
    context = {'job_info': job_info,'pt':pn }
    return render(request,'products/job_detail.html',context)






@login_required  
def jobAccepted(request,id):
    artisan = [Artisan.objects.get(user=request.user)]
    idn =id
    if ServiceRequest.objects.get(id=id, ordered=True,status='Paid'):

        accepted_job= ServiceRequest.objects.filter(id=id, ordered=True,status='Paid')
        for b in accepted_job:
            #b.artisan.set(artisan)
            b.artisan =Artisan.objects.get(user=request.user)
            b.save()
            #b.taken=True
         
            #b.save()
        ServiceRequest.objects.filter(id=id, ordered=True,status='Paid').update(accepted ="Accepted" ,
        accepted_date =timezone.now())
         
    #else:
       
     
    if ViewedJob.objects.filter(user=request.user,job_order_id=id).exists():

        current_job = ViewedJob.objects.filter(user=request.user,job_order_id=id)
        #current_job = ViewedJob.objects.filter(user=request.user,job_order_id=id).last()
        ViewedJob.objects.filter(user=request.user,job_order_id=id).update(accepted ="Accepted" ,
        accepted_date =timezone.now())

       
        return redirect('account:artisanPage')
        

    return redirect('/')
                       
                    





    



def currentJob(request):
    user=request.user  
   
    if not ViewedJob.objects.filter(user=user,accepted='Accepted').exists():
            messages.info(request,'You dont have any on going job yet!Go to dashboard and select a job to do')
            return render(request,'artisans/no_service_rendered.html')

    if ViewedJob.objects.filter(user=user,accepted='Accepted').exists():
        current_job = ViewedJob.objects.filter(user=user,accepted='Accepted').last()
        if current_job.work_done == True:
            messages.info(request,'This job is concluded already')


        context ={'current_job':current_job}
    return render(request,'artisans/current_job.html',context)




def CurrentJobInfo(request):
    user = request.user

    if not ViewedJob.objects.filter(user=user,accepted='Accepted').exists():
            messages.info(request,'You dont have any job to confirm here!Go to dashboard and select a job to do')
            return render(request,'artisans/no_service_rendered.html')

    elif ViewedJob.objects.filter(user=user,accepted='Accepted').exists():
        try:

            jobinfo = ViewedJob.objects.filter(user=user,accepted='Accepted').last()
            if jobinfo.work_done == True:
                messages.info(request,'Job already registered for payment')
                return redirect('account:artisanPage')

                
    
        except:
            raise Http404
        return render(request, 'artisans/currentjobinfo.html', {'jobinfo':jobinfo})

    




def completeJob(request,id):

    user = request.user
    artisan = Artisan.objects.get(user=request.user)

    if ViewedJob.objects.filter(user=user,accepted='Accepted',job_order_id=id,work_done=True).exists():
        messages.info(request,'Job already registered for payment. Pick up another job today.')
        return render(request,'artisans/no_service_rendered.html')

    elif ViewedJob.objects.filter(user=user,accepted='Accepted',job_order_id=id):

        if ServiceRequest.objects.filter(id=id,artisan =artisan, ordered=True,status='Paid',accepted ="Accepted"):
            ViewedJob.objects.filter(user=user,accepted='Accepted',job_order_id=id).update(work_done=True)
            ServiceRequest.objects.filter(artisan=artisan, ordered=True,status='Paid',accepted ="Accepted",id=id).update(work_done=True)

            return redirect('artisan:congratulation')

        else:
            messages.info(request,'Service Item not found')
            return render(request,'artisans/no_service_rendered.html')
    else:
        messages.info(request,'Service not accepted yet.Contact the admin')  
        return render(request,'artisans/no_service_rendered.html')      

           

        



def congratulations(request):
    messages.info(request,'Congratulations! Your payment is under processing') 
    return render(request,'artisans/congrats.html')

  




def artisan_services(request):
    user = Artisan.objects.get(user=request.user)
    if not ServiceRequest.objects.filter(artisan=user,accepted='Accepted',work_done=True).exists():
        messages.info(request,'You dont have any recorded service yet.Go to Jobs in your neigborhood and select a job')
        return render(request,'artisans/no_service_rendered.html')

    elif ServiceRequest.objects.filter(artisan=user,accepted='Accepted',work_done=True).exists():
        job_info = ServiceRequest.objects.filter(artisan=user).order_by('-date_created')

        context ={'job_info':job_info}
        return render(request,'artisans/completed_services.html',context)

    messages.info(request,'No Job done yet')    
    return render(request,'artisans/completed_services.html')    










class ListArtisansAvailable(DetailView):
    model: Artisan
    template_name ="artisans/artisan-search.html"


    def get_context_data(self,*args, **kwargs):
        context= super(ListArtisansAvailable,self).get_context_data(*args,**kwargs)

        context["items"] = Artisan.objects.filter(Q(profession_name__icontains ="name"))
        return context




def artisanList(request, pk):
    # icontains here
    if Artisan.objects.filter(profession_name=pk).exists():
        details = Artisan.objects.filter(profession_name=pk)
        context={"details":details}
        
        return render(request, "artisans/artisan-search.html", context)
    else:
        
        context={'name':pk}
        messages.warning(request, pk,"is not available at this point")
        return render(request, "artisans/artisan-search.html", context)




def artisanRequest(request, pk):
    services = Artisan.objects.get(pk=pk)  
    job = services.profession_name 
    item = Product.objects.get(name=job)
    if item:

        context ={"services":services,"item":item}
        return render(request ,'artisans/artisan_request.html',context) 

    messages.warning(request,'No such service available')
    return redirect ('/')    









class SearchFlipView(TemplateView):
    model: Artisan
    template_name ="artisans/artisan-search.html"


    def get_queryset(self, **kwargs):
        context= super().get_queryset(**kwargs)

        context["items"] = Artisan.objects.filter(Q(profession_name__icontains ="q"))
        return context
            

def searchResult(request):
    query = request.POST.get('q')
    item = Artisan.objects.filter(Q(profession_name__icontains=query))

    
    context ={'item':item,'query':query}
    if item:
        return render(request,"artisans/artisan-search.html",context)

    else:
        messages.warning(request,'Service not available at this time')
        return redirect('/')   










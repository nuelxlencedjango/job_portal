
#from turtle import title
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render,redirect

from django.http import Http404
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from products .models import *
from django.db.models import Q 

from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView ,DetailView,
)
from .forms import *


# Create your views here.

#artisan registration
def artisanRegistration(request):
    if request.method == 'POST':
        #input taking-basic and detailed information
        form1 = CreateUserForm(request.POST)
        form4 = WorkersForm(request.POST,request.FILES) 
        
        #check both basic and detailed data to verify the validity
        if form1.is_valid() and form4.is_valid():
            user = form1.save()
            profile = form4.save(commit=False)
            
            #associate detailed data to basic data of the user
            profile.user =user
            profile.save()
            img_obj = form4.instance
            id = form1.cleaned_data.get('id')
            messages.success(request, 'Account was created for ' , id)

            return redirect('account:login')
    #empty forms
    else:
        form1 =CreateUserForm()
        form4 = WorkersForm()
        
    context = {'form1':form1, 'form4': form4}   
    return render(request, 'account/artisan_register.html', context)



def confirmedOrders(request):
    return render(request ,'artisans/available_jobs.html')  


#updating artisan's data
@login_required
def artisan_update(request):
    if request.method =="POST":
        #taking data from the user
        form1 = UserUpdateForm(request.POST, instance = request.user)
        form4 = ArtisanUpdateForm(request.POST, request.FILES,instance = request.user.artisan)
        
        #check forms validity
        if form1.is_valid() and form4.is_valid():
            form1.save()
            form4.save()

            messages.success(request,"Successfully updated")
            return redirect('account:artisanPage')
               
        else:
            messages.warning(request,"Not updated")
    
    # empty form
    else:
        form1 = UserUpdateForm(instance = request.user)
        form4 = ArtisanUpdateForm(instance=request.user.artisan)          

    context = {'form1':form1, 'form4':form4}

    return render(request,'account/update_artisan_info.html',context)  




@login_required
def paidJobs(request):
    #the artisan
    artisan = Artisan.objects.filter(user=request.user)
   
    job_location = request.user.artisan.location
    #job type
    job_name   = request.user.artisan.profession_name

    #artisan job -first on the list
    if ServiceRequest.objects.filter(ordered=True,status='Paid',artisan=artisan[0]).exists():
        res=ServiceRequest.objects.filter(ordered=True,status='Paid',artisan=artisan[0])
        
        #jobs accepted by the artisan
        if ServiceRequest.objects.filter(ordered=True,status='Paid',artisan=artisan[0],accepted='Accepted').exists():
            messages.info(request ,"No new jobs avaialable now.")
            return render(request,'check.html')
            
        context ={'areaJobs':res}
        return render(request,'check.html',context) 

    #if artisan has no job available
    elif ServiceRequest.objects.filter(ordered=True,status='Paid',product=job_name).exists():        
        res =ServiceRequest.objects.filter(ordered=True,status='Paid',product=job_name)

        context ={'areaJobs':res}
        return render(request,'check.html',context) 
    
    else:
        messages.success(request, f"No {job_name} work available now.Please check back later.") 
        return render(request,'check.html')  



#job detail
@login_required
def jobDetail(request,id):
    #authenticate the user
    if request.user.is_authenticated:
        artisan = [Artisan.objects.filter(user=request.user)]
        
        #request id
        job_info= ServiceRequest.objects.filter(id =id)
        for job in job_info:
            pn =job.id
            
            #creating viwedjob object
            job_detail,create =ViewedJob.objects.get_or_create(user=request.user,
            job_name=job.product.name,category=job.product.category,
            description =job.description,price =job.get_service_rate(),client=job.user.last_name,address =job.address,
            date=job.date_created,phone=job.user.details.phone,job_order_id=job.id
        )
  
    context = {'job_info': job_info,'pt':pn }
    return render(request,'products/job_detail.html',context)



#artisan accepted jobs
@login_required  
def jobAccepted(request,id):
    artisan = [Artisan.objects.get(user=request.user)]

    #if service ordered is paid,get the job id and assign the artisan to it
    if ServiceRequest.objects.get(id=id, ordered=True,status='Paid'):
        accepted_job= ServiceRequest.objects.filter(id=id, ordered=True,status='Paid')

        for b in accepted_job:
            b.artisan =Artisan.objects.get(user=request.user)
            b.save()

        #update the service order to being accepted 
        ServiceRequest.objects.filter(id=id, ordered=True,status='Paid').update(accepted ="Accepted" ,
        accepted_date =timezone.now())
     
    #get job viwed by the artisan,add date to it
    if ViewedJob.objects.filter(user=request.user,job_order_id=id).exists():
        current_job = ViewedJob.objects.filter(user=request.user,job_order_id=id)
        ViewedJob.objects.filter(user=request.user,job_order_id=id).update(accepted ="Accepted" ,
        accepted_date =timezone.now())

        return redirect('account:artisanPage')
        
    return redirect('/')
                       
                    


@login_required
def currentJob(request):
    user=request.user  
   
   #on going job
    if not ViewedJob.objects.filter(user=user,accepted='Accepted').exists():
            messages.info(request,'You dont have any on going job yet!Go to dashboard and select a job to do')
            return render(request,'artisans/no_service_rendered.html')

    #if accepted,get the last one
    if ViewedJob.objects.filter(user=user,accepted='Accepted').exists():
        current_job = ViewedJob.objects.filter(user=user,accepted='Accepted').last()
        if current_job.work_done == True:
            messages.info(request,'This job is concluded already')

        context ={'current_job':current_job}
    return render(request,'artisans/current_job.html',context)



#view current job
@login_required
def CurrentJobInfo(request):
    user = request.user
    #if artisan has not accepted ,he no current
    if not ViewedJob.objects.filter(user=user,accepted='Accepted').exists():
            messages.info(request,'You dont have any job to confirm here!Go to dashboard and select a job to do')
            return render(request,'artisans/no_service_rendered.html')

    # accepted jobs
    elif ViewedJob.objects.filter(user=user,accepted='Accepted').exists():
        try:
            jobinfo = ViewedJob.objects.filter(user=user,accepted='Accepted').last()
            if jobinfo.work_done == True:
                messages.info(request,'Job already registered for payment')
                return render(request,'payments/payment_underway.html')

                
        except:
            raise Http404
        return render(request, 'artisans/currentjobinfo.html', {'jobinfo':jobinfo})

    


#job completed
@login_required
def completeJob(request,id):
    user = request.user
    #artisan user
    artisan = Artisan.objects.get(user=request.user)
     
    #all work done jobs
    if ViewedJob.objects.filter(user=user,accepted='Accepted',job_order_id=id,work_done=True).exists():
        messages.info(request,'Job already registered for payment. Pick up another job today.')
        return render(request,'artisans/no_service_rendered.html')

    #work accepted nut not completed yet
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

           
#conformation of registration        
def congratulations(request):
    messages.info(request,'Congratulations! Your payment is under processing') 
    return render(request,'artisans/congrats.html')

  
#artisan servies 
def artisan_services(request):
    user = Artisan.objects.get(user=request.user)
    # if artisan has no job done 
    if not ServiceRequest.objects.filter(artisan=user,accepted='Accepted',work_done=True).exists():
        messages.info(request,'You dont have any recorded service yet.Go to Jobs in your neigborhood and select a job')
        return render(request,'artisans/no_service_rendered.html')
    
    #else ,if he has jobs completed
    elif ServiceRequest.objects.filter(artisan=user,accepted='Accepted',work_done=True).exists():
        job_info = ServiceRequest.objects.filter(artisan=user,accepted='Accepted',work_done=True).order_by('-date_created')
        

        context ={'job_info':job_info}
        return render(request,'artisans/completed_services.html',context)

    messages.info(request,'No Job done yet')    
    return render(request,'artisans/completed_services.html')    



#list of artisans
def artisanList(request, pk):
    #all artsan of a particular trade
    if Artisan.objects.filter(profession_name=pk).exists():
        details = Artisan.objects.filter(profession_name=pk)
        for i in details:
            title =i.profession_name

        context={"details":details,'title':title}
        
        return render(request, "artisans/artisan-search.html", context)
    else:
        
        messages.warning(request, pk,"is not available at this point")
        return render(request, "artisans/artisan-search.html")



def artisanRequest(request, pk):
    #artisan detail
    services = Artisan.objects.get(pk=pk)  
    # artsan job service
    job = services.profession_name 
    item = Product.objects.get(name=job)
    if item:

        context ={"services":services,"item":item}
        return render(request ,'artisans/artisan_request.html',context) 

    messages.warning(request,'No such service available')
    return redirect ('/')    


#earches
class SearchFlipView(TemplateView):
    model: Artisan
    template_name ="artisans/artisan-search.html"
    
    #searching a particular job
    def get_queryset(self, **kwargs):
        context= super().get_queryset(**kwargs)

        context["items"] = Artisan.objects.filter(Q(profession_name__icontains ="q"))
        return context



# user's bank details
@login_required(login_url='/account/login')
def bankDetails(request):
    form = BankDetailForm()
    if request.method == 'POST':
        #input from the user
        form = BankDetailForm(request.POST)
        if form.is_valid():
                job_obj = form.save(commit=False)
                job_obj.user = request.user
                job_obj.save()
                return redirect('account:artisanPage')
                
    context={'form': form}
    return render(request, 'artisans/bank_info.html', context) 


#artisan outstanding detail
@login_required
def outstandingPay(request):
    #outstanding pay
    out_standing =  ViewedJob.objects.filter(user=request.user,accepted='Accepted',work_done=True).last()
    price = out_standing.price
    
    context={'price':price}
    return render(request,'check.html',context)



def JobList(request):
    #list of job completed by the artisan
    no_job =  ServiceRequest.objects.filter(artisan=Artisan.objects.get(user=request.user),accepted='Accepted',ordered=True,status='Paid',work_done=True).count()
    context={'no_job':no_job}
    return render(request,'check.html',context)



#updating artisan's information
@login_required
def update_bank_info(request):
    if request.method =="POST":

        form = BankUpdateForm(request.POST,instance = request.user.artisan_bank)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully updated")
            return redirect('account:artisanPage')
               
        else:
            messages.warning(request,"Not updated")
    
    else:
        form = BankUpdateForm(instance=request.user.artisan_bank)  
                
    context = {'form':form}

    return render(request,'artisans/bank_update_form.html',context)  
     

  

    
    







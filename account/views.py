from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required


from products.models import *
from artisan .models import *

from .models import *
from .forms import *

# Create your views here.


#type of users
def registration(request):
    return render(request,'account/registration.html')



# client registration
def registerPage(request):
    if request.method == 'POST':
        # client detail intake
        form1 = CreateUserForm(request.POST)
        form2 = CustomerForm(request.POST)
         
         #check data given validity
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            #associate detail information to the user before saving
            profile = form2.save(commit=False)
            profile.user =user
            profile.save()

            id = form1.cleaned_data.get('id')

            messages.success(request, 'Account successfully created ' , id)

            return redirect('products:home')
    else:
        form1 =CreateUserForm()
        form2 = CustomerForm()

    messages.success(request, 'Account was created for')    
    context = {'form1':form1, 'form2': form2}   
    return render(request, 'account/register.html', context)





# client and artisan loggining into account
def loginPage(request):
    if request.method == 'POST':
        #taking input from the user
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        #authenticate the user and log the user in if authenticated and exists
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if Customer.objects.filter(user = user).exists():
                login(request,user)
                return redirect('products:home')
            
            # if the user is an artisan and already registered,log him in
            elif Artisan.objects.filter(user = user).exists():
                login(request,user)
                return redirect('account:artisanPage')
               
           #if user is a superuser
            elif user.is_superuser:
                login(request,user)
                return redirect('account:admin_page')
        
        #if none is correct,username or password is incorrect
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'account/login.html', context)



#logout 
@login_required
def logoutPage(request):
    logout(request)
    return redirect('products:home')


# login to update information
@login_required
def update_info(request):
    if request.method =="POST":
        #taking user details
        form1 = UserUpdateForm(request.POST, instance = request.user)
        form2 = CustomerUpdateForm(request.POST, request.FILES,instance = request.user.details)
         #if data given are correct,update
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()

            messages.success(request,"Successfully updated")
            return redirect('products:dashboard')
            
         #if not correct,a warning message  
        else:
            messages.warning(request,"Not updated")
    
    else:
        form1 = UserUpdateForm(instance = request.user)
        form2 = CustomerUpdateForm(instance=request.user.details)          

    context = {'form1':form1, 'form2':form2}

    return render(request,'account/update_info.html',context)  



#login to see all orders,customers 
@login_required
def adminPage(request):
    orders = OrderItem.objects.all()
    ord_product =Order.objects.all()
    customers = Customer.objects.all()
    total_customers =customers.count()
    total_orders =orders.count()

    completed =orders.filter(status='Completed')
    pending =orders.filter(status='pending')

    completed_job =orders.filter(status='Completed').count()
    pending_job =orders.filter(status='pending').count()

    context={
        'orders':orders,
        'cutomers':customers,
        'total_customers':total_customers,
        'total_orders':total_orders,
        ' completed ':completed,
        'pending':pending,
        'completed_job':completed_job,
        'pending_job':pending_job,
        'ord_product':ord_product

        
    }
    return render(request ,'admin/admin_dashboard.html',context)    



#client registration
def clientRegister(request):
    if request.method == 'POST':
        #get input from client
        form1 = CreateUserForm(request.POST)
        form2 = CustomerForm(request.POST)
        
        #check is data given is valid
        if form1.is_valid() and form2.is_valid():
            #save form 1
            user = form1.save()
            #associate form 2 to the user before saving
            profile = form2.save(commit=False)
            profile.user =user
            profile.save()

            id = form1.cleaned_data.get('id')

            messages.success(request, 'Account successfully created ' , id)

            return redirect('account:login')

    else:
        form1 =CreateUserForm()
        form2 = CustomerForm()
        
        
    messages.success(request, 'Account was created for')    
    context = {'form1':form1, 'form2': form2}   
    return render(request, 'dashboard/client/index.html', context)





def clientDashboard(request):
    return render(request,'dashboard/client/clients.html')   



#artisan dashboard
def artisanDashboard(request):
    #artisan name
    job_name   = request.user.artisan.profession_name
    
    #all jobs done by the artisan
    no_job = ServiceRequest.objects.filter(artisan=Artisan.objects.get(user=request.user),accepted='Accepted',ordered=True,status='Paid',work_done=True)
    #last viewed job
    out_standing =  ViewedJob.objects.filter(user=request.user,accepted='Accepted',work_done=True).last()
    price = out_standing.price
    
    #number of job done
    no_job =  ServiceRequest.objects.filter(artisan=Artisan.objects.get(user=request.user),accepted='Accepted',ordered=True,status='Paid',work_done=True).count()
   
    #available jobs
    areaJobs=ServiceRequest.objects.filter(ordered=True,status='Paid',product=job_name)

    context={'no_job':no_job,'price':price,'areaJobs':areaJobs}
    return render(request,'dashboard/artisan/artisans_admin.html',context)







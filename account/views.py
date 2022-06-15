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
from products.models import *
from django.contrib.auth.models import Group
#from .filters import OrderFilter
from artisan .models import *

from .models import *
from .forms import *

# Create your views here.

def registration(request):
    return render(request,'account/registration.html')



#@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            #obj = Customer.objects.get(user=user.id)
            if Customer.objects.filter(user = user).exists():
                login(request,user)
                return redirect('products:home')

            elif Artisan.objects.filter(user = user).exists():
                login(request,user)
                return redirect('artisan:confirmed_orders')
           

           #work on this
            elif username =="iwanwok" and password =="iwanwok":
                login(request,user)
                return redirect('account:admin_page')

        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'account/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('products:home')


#def adminLoginPage(request):
   # if request.method == 'POST':
     #   username = request.POST['username']
       # password =request.POST['password']
        
       # user = authenticate(request, username=username, password=password)
 
       # if user is not None:
        #    login(request, user)
         #   return redirect('account:admin_page')
        #else:
         #   messages.info(request, 'Username OR password is incorrect')

   # context = {}
   # return render(request, 'account/login.html', context)


def registerPage(request):
    if request.method == 'POST':
        form1 = CreateUserForm(request.POST)
        form2 = CustomerForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            profile = form2.save(commit=False)
            profile.user =user
            profile.save()

            id = form1.cleaned_data.get('id')

            messages.success(request, 'Account successfully created ' , id)

            return redirect('account:dashboard')


    else:
        form1 =CreateUserForm()
        form2 = CustomerForm()
        
        
    messages.success(request, 'Account was created for')    
    context = {'form1':form1, 'form2': form2}   
    return render(request, 'account/register.html', context)




def update_info(request):
    if request.method =="POST":

        form1 = UserUpdateForm(request.POST, instance = request.user)
        form2 = CustomerUpdateForm(request.POST, request.FILES,instance = request.user.details)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()

            messages.success(request,"Successfully updated")
            return redirect('products:orderlist')
            
           
        else:
            messages.warning(request,"Not updated")
    
    else:
        form1 = UserUpdateForm(instance = request.user)
        form2 = CustomerUpdateForm(instance=request.user.details)          

    context = {'form1':form1, 'form2':form2}

    return render(request,'account/update_info.html',context)  



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
    return render(request ,'admin_dashboard.html',context)    




    #new 



def clientRegister(request):
    if request.method == 'POST':
        form1 = CreateUserForm(request.POST)
        form2 = CustomerForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
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
    return render(request,'dashboard/client/index.html')    
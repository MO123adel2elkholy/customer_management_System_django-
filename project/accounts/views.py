from django.shortcuts import render , redirect, HttpResponseRedirect , HttpResponse
from django.http import HttpResponse
from  .models import *
from .forms import Orderform, CreateUserForm, CustomerForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_user , allowed_user, admin_only
from django.contrib.auth.models import Group
# Create your views here.


def home(request):
    return render(request , 'accounts/home.html')

@unauthenticated_user
def register(request):
        form = CreateUserForm()
        if request.method == 'POST':
            print('Data', request.POST)
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                username = form.cleaned_data.get('username')

                messages.success(request, 'success created your account ' + str(username))
                return redirect('login')
        data = {"form": form}
        return render(request, 'accounts/register.html', data)



@unauthenticated_user
def log(request):
      return render(request, 'accounts/login.html')


# def user_profile(request, user_name):
#     return render(request, 'profil.html', {'username': user_name})


def login_backend(request):
    u = request.POST['user_name']
    p = request.POST['password']
    loged = authenticate(username=u, password=p)
    if loged is not None:
        login(request, loged)
        return redirect('/')
    else:
       return HttpResponse('wrong password')

def logout_backend(request):
    logout(request)
    # return render(request, 'accounts/login.html')
    return HttpResponseRedirect('/login')
@login_required(login_url='login/')
@allowed_user(allowed_roles=['admins'])
def customer(request , pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = customer.order_set.all().count()
    myfilter = OrderFilter(request.GET , queryset=orders)
    orders=myfilter.qs
    data = {"customer" : customer , "orders" : orders , "orders_count" : orders_count, "myfilter":myfilter}
    return render(request , 'accounts/Customer.html' , data)
@login_required(login_url='login/')
@allowed_user(allowed_roles=['admins'])
def profile(request):
    products = Product.objects.all()
    data={"products" : products}
    return render(request , 'accounts/profile.html' , data)
@login_required(login_url='login/')
@admin_only
def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = Order.objects.all().count()
    delivered = Order.objects.all().filter(status='delvired').count()
    pending = Order.objects.all().filter(status='pending').count()
    data = {"customers": customers, "order":orders ,
            'delvired' : delivered , 'pending' : pending
        ,"total_order" :total_orders}
    return render(request , 'accounts/dashboard.html' , context=data)
@login_required(login_url='login/')
@allowed_user(allowed_roles=['admins'])
def createorder(request, pk):
    orderformset = inlineformset_factory(Customer, Order, fields=( 'product','status' ) , extra=5)
    customer = Customer.objects.get(id=pk)
    formset = orderformset( queryset=Order.objects.none(), instance=customer)
    #form = Orderform(initial={'customer' : customer})
    formset = orderformset(instance=customer)
    if request.method=='POST':
        print('Data' , request.POST)
        formset = orderformset(request.POST, instance=customer)
       # form = Orderform(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    data ={'formset' : formset}
    return render(request, 'accounts/order_forms.html' , data)

@login_required(login_url='login/')
@allowed_user(allowed_roles=['admins'])
def update_order(request , pk):
    order = Order.objects.get(id=pk)
    form = Orderform(instance=order)
    if request.method=='POST':
        print('Data' , request.POST)
        form = Orderform(request.POST , instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    data = {'form': form}
    return render(request, 'accounts/order_forms.html', data)

@login_required(login_url='login/')
@allowed_user(allowed_roles=['admins'])
def delete_order(request , pk ):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    return render(request, 'accounts/delete_order.html' , {'item': order})


@login_required(login_url='login/')
@allowed_user(allowed_roles=['customers'])
def user(request):
    orders= request.user.customer.order_set.all()
    total_orders = request.user.customer.order_set.all().count()
    delivered = request.user.customer.order_set.all().filter(status='delvired').count()
    pending = request.user.customer.order_set.all().filter(status='pending').count()
    print('your orders' , orders)
    data={"orders" :orders , "order":orders ,
            'delvired' : delivered , 'pending' : pending
        ,"total_order" :total_orders  }
    return render(request,'accounts/user.html' , data)

@login_required(login_url='login/')
@allowed_user(allowed_roles=['customers'])
def account_setting(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method=='POST':
        form = CustomerForm( request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    data={'form': form }
    return render(request,'accounts/account_setting.html' , data)
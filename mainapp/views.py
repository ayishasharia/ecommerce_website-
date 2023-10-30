from django.shortcuts import render,redirect
from .models import user_1,product_model,cart_Model,cart_item
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from math import ceil
from django.contrib.auth.decorators import login_required
def index(request):
    username=request.user.username
    return render(request,'index.html',{'username': username})
def cart(request):
    username=request.user.username
    return render(request,'cart.html',{'username': username})
def shop(request):
    username=request.user.username
    return render(request,'shop.html',{'username': username})


def register(request):
    if request.method =='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        dob=request.POST.get('dob')
        
        phone=request.POST['phone']
        address=request.POST.get('address')
        email=request.POST.get('email')
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        # print(fname,lname,gender,phone,dob,district,phone,address,uname,password,cpassword)
        # print("success")
        if User.objects.filter(username=uname).exists():
            # user alrdy exist chyyunnundenkl again register avanda adin uname alrdy undo check chyyunnu
            print("username exists")
            return render(request,'register.html')
        else:
            
            user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password,email=email)
            user.save()
            newuser=user_1(UserF=user,gender=gender,phone=phone,dob=dob,address=address)
            newuser.save()
            print("success")
            
            user=authenticate(username=uname, password=password)
            if user is not None:
                login(request,user)
                return redirect('loginpage')
            # return redirect('registration')
    return render(request,'register.html')
            
    
    
def logins(request):
    if request.method == 'POST':
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        user=authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)
            
                
            
            print("logined successfully")
            
            
            return redirect('indexpage')
        else:
            print("login wasnt successfull")
            return render(request, 'login.html')
    return render(request,'login.html')
    
def nav(request):
    return render(request,'nav.html')

def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')

def handle_logout(request):
    logout(request)
    
    return redirect('loginpage')

def view_products(request):
    # allProds = []
    # catprods = product_model.objects. values('p_category', 'p_id')
    # cats = {item ['p_category'] for item in catprods} 
    # for cat in cats:
    #     prod= product_model.objects.filter(p_category=cat)
    #     n=len(prod)
    #     nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #     allProds.append([prod, range(1, nSlides), nSlides])
    # params= {'allProds' :allProds}

    # return render(request,'shop.html', params)
    p=product_model.objects.all()
    return render(request,'shop.html',{'details':p})
@login_required(login_url='loginpage')
def cart(request):
    current_user=request.user
    crt=cart_Model.objects.get(user=current_user)
    cart_items=crt.items.all()
    sub_total=0
    for s in cart_items:
        sub_total=(s.quantity)*(s.item.p_price)
    total=0
    for c in cart_items:
        total=total+((c.quantity)*(c.item.p_price))
    return render(request,'cart.html',{'cart_item':cart_items,'total':total,'sub_total':sub_total})

def add_to_cart(request,i):
    current_user=request.user
    item=product_model.objects.get(id=i)
    qty=1
    price=item.p_price
    try:
        user_cart=cart_Model.objects.get(user=current_user)
        new_cart_item=cart_item(item=item,quantity=qty,price=price)
        new_cart_item.save()
        user_cart.items.add(new_cart_item)
        user_cart.save()
    except:
        user_cart=cart_Model(user=current_user)
        user_cart.save()
        new_cart_item=cart_item(item=item,quantity=qty,price=price)
        new_cart_item.save()
        user_cart.items.add(new_cart_item)
        user_cart.save()
    return redirect('cartpage')

def removeall_from_cart(request):
    current_user=request.user
    crt=cart_Model.objects.get(user=current_user)
    cart=crt.items.clear()
    return render(request,'cart.html')

def remove_item(request,item_id):
    current_user=request.user
    user_cart=cart_Model.objects.get(user=current_user)
    item=cart_item.objects.get(id=item_id)
    user_cart.items.remove(item)
    user_cart.save()
    return redirect('cartpage')

def my_view(request):
    if request.user.is_authenticated:
        # User is logged in, perform actions for authenticated users
        return render(request, 'index.html')
    else:
        # User is not logged in, perform actions for anonymous users
        return render(request, 'index.html')

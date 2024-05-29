from django.shortcuts import redirect, render
from combon.models import Emp, Dhan
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from combon.forms import  EmpForm, LoginForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.cache import cache_control

def signup(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        us=request.POST['username']
        pa=request.POST['password']
        use =User.objects.create_user(username=us, password=pa)
        Dhan.objects.filter(user=use).update(phoneno=request.POST['phoneno'],dob=request.POST['dob'],address=request.POST['address'])
        # if form.is_valid():
        #     form.save()
        return redirect("/")
    else:
        form = LoginForm()
    return render(request,'signup.html', {'form': form})
        

def homepage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
                form.save() 
                return redirect("/show")
    else:
        form = UserCreationForm()
    return render(request,"homepage.html",{'form':form})

def login_user(request):
    if request.method == 'POST':
       use=request.POST['user_name']
       use2=request.POST['user_password']
       use3=authenticate(request,username=use, password=use2)
       if use3:
           login(request, use3)
           return redirect('/crud_home')
       else:
           return HttpResponse('Invalid User name or password')
       
    else:
           return render(request,"login.html")
    
          
def show(request):
    dha= Dhan.objects.all()
    return render(request,'show.html',{'dha':dha})


@login_required(login_url="/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def addnew(request):  
    if request.method == "POST":  
        form= EmpForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('/crud_display') 
    else:  
        form = EmpForm()  
    return render(request,'crud_home.html',{'form':form})  

def inde(request):  
    crs = Emp.objects.all()  
    return render(request,"crud_display.html",{'crs':crs})  

def edit(request,id):  
    crs = Emp.objects.get(id=id)  
    return render(request,'edit.html', {'crs':crs})  

def update(request,id):  
    crs = Emp.objects.get(id=id)  
    form= EmpForm(request.POST, instance=crs)  
    if form.is_valid():  
        form.save()  
        return redirect('/crud_display')  
    return render(request, 'edit.html', {'crs':crs})  
     
def destroy(request,id):  
    crs = Emp.objects.get(id=id)  
    crs.delete()  
    return redirect('/crud_display')

def logout_view(request):
    logout(request)
    return redirect("/")

# signup_crud

def signup_inde(request):  
    sgn = Dhan.objects.all()  
    return render(request,"show.html",{'sgn':sgn})  

def signup_edit(request,id):  
    sgn = User.objects.get(id=id)  
    return render(request,'signup_edit.html', {'sgn':sgn})  

# def signup_update(request,id):  
#     sgn, created = Dhan.objects.get_or_create(user=request.user)  
#     form= LoginForm(request.POST, instance=sgn)
#     if request.method=='POST': 
#             if form.is_valid():  
#                 form.save()  
#                 return redirect('/show')  
#     return render(request, 'signup_edit.html', {'form':form})  
     
def signup_destroy(request,id):  
    sgn = User.objects.get(id=id)  
    sgn.delete()  
    return redirect('/show')

def signup_update(request,user_id):
    user = User.objects.get(pk=user_id)
    custom_user = Dhan.objects.get(user=user)
    
    if request.method == 'POST':
        form = LoginForm(request.POST, instance=custom_user)
        
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.save()
            custom_user.address = form.cleaned_data['address']
            custom_user.dob = form.cleaned_data['dob']
            custom_user.phoneno = form.cleaned_data['phoneno']
            custom_user.save()
        
            return redirect('/show')
    else:
        form = LoginForm(instance=custom_user)
    return render(request, 'show.html', {'form': form})

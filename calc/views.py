from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['password']
        User =auth.authenticate(username=username,password=password)
        if User is not None:
            auth.login(request,User)
            return redirect("/test")    
    else:    
        return render(request,"index.html")
def add(request):
    n1=int(request.GET["num1"])
    n2=int(request.GET["num2"])
    
    res=n1+n2   
    return render(request,"result.html",{"result":res})    
def registration(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['re_password']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("Username Already taken")
            
            elif User.objects.filter(email=email).exists():
                print("Email Already taken")
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()
        else:
            print("Password not matched")        
        return redirect('/test')
    return render(request,"register.html")   
def test(request):
    dests=Post.objects.all()
    return render(request,"home.html",{'dests':dests})   
def terminal(request):
    return render(request,"terminal.html")    
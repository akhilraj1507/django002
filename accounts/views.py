from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import extra

# Create your views here.
def sgn(request):
    if request.method=='POST':
        fun=request.POST['username']
        nm=request.POST['name']
        cn=request.POST['contact']
        fem=request.POST['email']
        pw=request.POST['password']
        pr=request.POST['repassword']
        if(pw==pr):
            if User.objects.filter(username=fun).exists():
                messages.info(request,'username already exist')
                return redirect('sign')
            else:
                usr=User.objects.create_user(username=fun,email=fem,password=pw)
                usr.save()
                ex=extra()
                ex.user=usr
                ex.name=nm
                ex.contact=cn
                ex.save()
                return redirect('login')

    return render(request,'signin.html')

def lgn(request):
    if request.method=='POST':
        fun=request.POST['username']
        pw=request.POST['password']
        user=auth.authenticate(username=fun,password=pw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'incorrect username or password')
            return redirect('sign')
            
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')




from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalide credentials")
            return  redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        usname=request.POST['username1']
        fsname=request.POST['first_name']
        lsname=request.POST['last_name']
        id=request.POST['email']
        pswrd=request.POST['password1']
        cpswrd=request.POST['password2']
        if pswrd==cpswrd:
            if User.objects.filter(username=usname).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=id).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=usname,password=pswrd,first_name=fsname,last_name=lsname,email=id)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

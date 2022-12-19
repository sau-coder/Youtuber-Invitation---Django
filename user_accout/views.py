from django.contrib.auth import logout
from django.shortcuts import render , redirect 
from django.contrib.auth.models import User 
from django.contrib import messages , auth

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password  = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request , user)
            messages.success(request , 'User logged in Successfully')
            return redirect('dashboard')
        else:
            messages.error(request , 'invalid credentials')
            return redirect('login')

    return render(request , 'users_accounts/login.html')


def register(request):
    if request.method == 'POST' :
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request , 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request , 'Email Already Exist')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name = firstname , last_name = lastname , username = username ,  email = email , password = password)
                    user.save()
                    messages.success(request , 'Account Created Successfully' )
                    return redirect('login')
        else:
            messages.error(request , 'Password does not match')
            return redirect('register')

    return render(request , 'users_accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect ('home')

def dashboard(request):
    return  render(request , 'users_accounts/dashboard.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def home(request):
    return render(request, 'webhome/index.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            
    
    context= {}
    return render(request, 'webhome/login.html', context)

def doctorlogin(request):
    return render(request, 'webhome/doctorlogin.html')

def profile(request):
    return render(request, 'webhome/profile.html')
     
def register(request):
    form = CreateUserForm()
    
    
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account wass created for' + user)
            return redirect('login')
        
        
    context ={'form':form}
    return render(request, 'webhome/register.html', context)
       
         

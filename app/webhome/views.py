from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'webhome/index.html')

def login(request):
    return render(request, 'webhome/login.html')

def doctorlogin(request):
    return render(request, 'webhome/doctorlogin.html')

def profile(request):
    return render(request, 'webhome/profile.html')

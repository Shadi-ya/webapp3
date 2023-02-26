from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('profile/', views.profile),
    path('doctorlogin/', views.doctorlogin),
    path('register/', views.register, name='register'),
]

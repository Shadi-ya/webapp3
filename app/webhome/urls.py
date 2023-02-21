from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('profile/', views.profile),
    path('doctorlogin/', views.doctorlogin),
    path('register/', views.register),
]

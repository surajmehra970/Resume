from django.contrib import admin
from django.urls import path
from Resume_front import views

urlpatterns = [
    path('', views.resume, name='home'),
    path('skill/', views.skill, name='skill'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    path('Donation/', views.Donetions, name='donation'),
]

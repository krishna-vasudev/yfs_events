from django.shortcuts import render,HttpResponse,redirect
from eventsapp.admin import Events
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib.auth.models import User

# Create your views here.

#functions to render templates for normal users
def events(request):
    context ={
        "Events":Events.objects.all()
    }
    return render(request,'eventsapp/events.html',context)


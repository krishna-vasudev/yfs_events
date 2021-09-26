from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from eventsapp import views

urlpatterns = [
    path("",views.events,name='events'),
]
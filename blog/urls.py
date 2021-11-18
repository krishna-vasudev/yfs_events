from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.recentblogs, name="recentblogs"),
    path("allblogs",views.allblogs,name="allblogs"),
    path("detailedblog/<str:pk>",views.detailedblog, name="detailedblog"),
    path("postcomments/<str:pk>",views.postcomments,name="postcomments"),
    path("hitlike/<str:pk>",views.hitlike, name="hitlike"),
]

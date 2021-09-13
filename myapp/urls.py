from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('userprofile/',userprofile,name='userprofile'),
    path('logout/',logout,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
]

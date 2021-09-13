from myapp.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            uid = User.objects.get(email=email)
            if uid.password == password:
                request.session['email'] = email
                return render(request,'dashboard.html')
            else:
                msg = 'Password does not matched'
                return render(request,'index.html',{'msg':msg})
        except:
            msg = 'Not Authorised email'
            return render(request,'index.html',{'msg':msg})
    else:
        return render(request,'index.html')

def userprofile(request):
    uid = User.objects.get(email= request.session['email'])
    return render(request,'user.html',{'uid':uid})

def logout(request):
    del request.session['email']
    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')
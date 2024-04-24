from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError,transaction
from accounts.models import KitchenOwner,Renter,Chife

# Create your views here.
def register_user(request:HttpRequest):

    return render(request,'accounts/register.html')


def login_user(request:HttpRequest):
    msg = None

    if request.method == "POST":
    
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            return redirect("main:home")
        else:
            msg = "Username or Password is wrong. Try again..."
    

    return render(request, "accounts/login_user.html", {"msg" : msg})

def logout_user(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login')
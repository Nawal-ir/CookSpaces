from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def home(requset:HttpRequest):
    
    if requset.user.is_authenticated:
        print(requset.user.first_name)
    
    return render(requset, "main/home.html")

def all_kitchen(requset:HttpRequest):
    
    return render(requset, "main/all_kitchen.html")

def kitchen_detail(requset:HttpRequest):
    
    return render(requset, "main/kitchen_detail.html")

def delete_kitchen(requset:HttpRequest):
    pass

def articals(requset:HttpRequest):
    
    return render(requset, "main/articals.html")

def about(requset:HttpRequest):
    
    return render(requset, "main/about.html")

def contact(requset:HttpRequest):
    
    return render(requset, "main/contact.html")

def add_review(requset:HttpRequest):
    pass
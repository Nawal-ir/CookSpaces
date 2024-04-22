from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def home(requset:HttpRequest):
    
    return render(requset, "main/home.html")
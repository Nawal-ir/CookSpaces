from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact, Artical, Review
from KitchenOwner.models import Kitchen, Equipment
from Renters.models import BookMark
import math

def home(request:HttpRequest):
    
    if request.user.is_authenticated:
        print(request.user.first_name)
    
    return render(request, "main/home.html")

def all_kitchen(request:HttpRequest):
    
    kitchens = Kitchen.objects.all()
    
    #calculate the page content
    limit = 4
    pages_count = [str(n) for n in range(1, math.ceil(kitchens.count()/limit)+1)] #use list comprehension to convert number to string number
    start = (int(request.GET.get("page", 1))-1)*limit
    end = (start)+limit
    
    #apply the limit/slicing
    kitchens = kitchens[start:end]

    # print(start, end)
    return render(request, "main/all_kitchen.html", {"kitchens" : kitchens, "pages_count":pages_count})


def kitchen_detail(request:HttpRequest, kitchen_id):

    try:
        #getting a  post detail
        kitchen = Kitchen.objects.get(pk=kitchen_id)
        reviews = Review.objects.filter(kitchen=kitchen) #this is to get the comments on the above post using filter
        is_saved = request.user.is_authenticated and  BookMark.objects.filter(user=request.user, kitchen=kitchen).exists()
    except Kitchen.DoesNotExist:
        return render(request, "404.html")
    except Exception as e:
        print(e)


    return render(request, "kitchenowner/kitchen_details.html", {"kitchen" : kitchen, "reviews" : reviews, "is_saved" : is_saved})

def delete_kitchen(request:HttpRequest, kitchen_id):

    #limit access to this view for only staff
    if not request.user.is_staff:
        return render(request, "no_permission.html")

    try:
        kitchen = Kitchen.objects.get(pk=kitchen_id)
        kitchen.delete()
    except Exception as e:
        print(e)
    

    return redirect("main:home")

def articals(request:HttpRequest):
    
    kitchens = Kitchen.objects.all()
    
    #calculate the page content
    limit = 4
    pages_count = [str(n) for n in range(1, math.ceil(kitchens.count()/limit)+1)] #use list comprehension to convert number to string number
    start = (int(request.GET.get("page", 1))-1)*limit
    end = (start)+limit
    
    #apply the limit/slicing
    kitchens = kitchens[start:end]

    # print(start, end)

    return render(request, "main/articals.html", {"kitchens" : kitchens, "pages_count":pages_count})


def about(request:HttpRequest):
    
    return render(request, "main/about.html")

def contact(request:HttpRequest):
    
    return render(request, "main/contact.html")

def add_review(request:HttpRequest):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    if request.method == "POST":
        try:
            recipes= Recipes.objects.get(pk=recipes_id)
            new_comment = Comment(Recipes=recipes,
                                  user=request.user, 
                                  content=request.POST["content"],
                                  evaluation=request.POST["evaluation"])
            new_comment.save()
        except Exception as e:
                print(e)
    
    return redirect("main:detail_recipes", recipes_id=recipes.id)

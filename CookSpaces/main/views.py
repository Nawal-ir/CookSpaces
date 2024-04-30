from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact, Article, Review
from KitchenOwner.models import Kitchen, Equipment
from Renters.models import BookMark
import math

def home(request:HttpRequest):
    
    if request.user.is_authenticated:
        print(request.user.first_name)
    
    return render(request, "main/home.html")

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

def all_article(request:HttpRequest):
    
    kitchens = Article.objects.all()
    
    # #calculate the page content
    # limit = 4
    # pages_count = [str(n) for n in range(1, math.ceil(kitchens.count()/limit)+1)] #use list comprehension to convert number to string number
    # start = (int(request.GET.get("page", 1))-1)*limit
    # end = (start)+limit
    
    # #apply the limit/slicing
    # kitchens = kitchens[start:end]

    # # print(start, end)
    
# "pages_count":pages_count
    return render(request, "main/articles.html", {"kitchens" : kitchens })

def about(request:HttpRequest):
    
    return render(request, "main/about.html")

def contact(request:HttpRequest):
        if request.method == 'POST':
            try:
                new_con = Contact(
                    user = request.user,
                    first_name = request.POST["first"],
                    last_name = request.POST["last"],
                    email = request.POST["email"],
                    message = request.POST['message']
                )
                new_con.save()
                
            except Exception as e:
                print(e)
            
            # return redirect('main:message')
        return render(request, "main/contact.html")

def messages(request:HttpRequest):

    if not request.user.is_superuser:
        return render(request, "no_permission.html")

    message = Contact.objects.all()[0:3]

    return render(request,'main/messages.html', {'message' : message})

def add_review(request:HttpRequest, kitchen_id):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    if request.method == "POST":
        try:
            kitchens= Kitchen.objects.get(pk=kitchen_id)
            new_review = Review(kitchen=kitchens,
                                  user=request.user, 
                                  content=request.POST["content"],
                                  evaluation=request.POST["evaluation"])
            new_review.save()
        except Exception as e:
                print(e)
    
    return redirect("KitchenOwner:kitchen_details", kitchen_id=kitchens.id)

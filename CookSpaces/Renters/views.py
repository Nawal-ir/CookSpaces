from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError,transaction
from accounts.models import KitchenOwner,Renter,Chife

def register_renter(request:HttpRequest):
    msg = None

    if request.method == "POST":
        try:
            with transaction.atomic():
                
                new_user = User.objects.create_user(
                    username=request.POST["username"], 
                    email=request.POST["email"], 
                    first_name=request.POST["first_name"], 
                    last_name=request.POST["last_name"], 
                    password=request.POST["password"]
                    )
                new_user.save()

                register_renter = Renter(
                    user=new_user, 
                    about=request.POST["about"],
                    avatar=request.FILES.get("avatar", Renter.avatar.field.get_default()),
                    phone=request.POST["phone"]
                    )
                register_renter.save()

            return redirect("accounts:login")
        
        except IntegrityError as e:
            msg = "This username is already taken. Please choose a different username."
            print(e)

        except Exception as e:
            msg = f"Something went wrong. Please try again. {e}"
            print(e)
    
    return render(request, "renters/register_renter.html", {"msg" : msg})

def profile(request:HttpRequest, user_id):
    try:
        user=User.objects.get(id=user_id)
        user_profile = Renter.objects.get(user=user)
    except:
        return render(request, "404.html")

    return render(request, "renters/profile.html",{"user_profile": user_profile,})


def update_profile(request:HttpRequest):
    msg = None

    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    if request.method == "POST":
        
        try:

            with transaction.atomic():
                user:User = request.user

                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.email = request.POST["email"]

                user.save()
                
                try:
                    profile:Renter= user.renter
                except Exception as e:
                    profile =Renter(user=user)

                profile.about = request.POST["about"]
                profile.avatar = request.FILES.get("avatar", profile.avatar)

                profile.save()

                return redirect("renters:profile", user_id=user.id)

        except Exception as e:
            msg = f"Something went wrong {e}"
            print(e)

    return render(request, "renters/profile_update.html", {"msg" : msg})


def my_order(request:HttpRequest):
    
    return render(request, 'renters/my_order.html')

def booking(request:HttpRequest):
    
    return render(request, 'renters/booking.html')

def saved_kitchens(request:HttpRequest):
    
    return render(request, 'renters/saved_kitchens.html')
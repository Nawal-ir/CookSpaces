from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate
from django.db import IntegrityError,transaction
from accounts.models import KitchenOwner,Renter
from KitchenOwner.models import Kitchen 
from Renters.models import BookMark

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
                if not new_user.groups.filter(name='Renter').exists():
                    group = Group.objects.get(name="Renter")
                    new_user.groups.add(group)
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
        user_profile = User.objects.get(pk=user_id)
        
    except:
        return render(request, "404.html")

    return render(request, "renters/profile.html",{"user_profile": user_profile,})


def update_profile(request:HttpRequest, user_id):
    msg = None

    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    try: 
        user_info = User.objects.get(pk=user_id)
    except:
        return render(request, "404.html")
    
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

                return redirect("Renters:profile", user_id=user.id)

        except Exception as e:
            msg = f"Something went wrong {e}"
            print(e)

    return render(request, "renters/profile_update.html", {"user_info":user_info, "msg" : msg})


def my_order(request:HttpRequest):
    
    return render(request, 'renters/my_order.html')

def booking(request:HttpRequest):
    
    return render(request, 'renters/booking.html')


def add_remove_saved_view(request: HttpRequest, kitchen_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    try:
        kitchen = Kitchen.objects.get(pk=kitchen_id)

        saved_kitchen = BookMark.objects.filter(user=request.user, kitchen=kitchen).first()

        if not saved_kitchen:
            saved = BookMark(user=request.user, kitchen=kitchen)
            saved.save()
        else:
            saved_kitchen.delete()
    
    except Exception as e:
        print(e)

    return render(request, 'renters/saved_kitchens.html',kitchen_id=kitchen_id)

def saved_kitchens(request:HttpRequest , kitchen_id):
        message = None
        try:
            kitchen = Kitchen.objects.get(pk=kitchen_id)
            is_saved=request.user.is_authenticate and BookMark.objects.filter(user=request.user, kitchen=kitchen).exists()
        except Kitchen.DoesNotExist:
            return render(request, "404.html")
        except Exception as e:
            message = f"Something went wrong {e}"            
            print(e)
        

        return render(request, "renters/kitchen_datails.html", {"kitchen" :  kitchen,"is_saved" : is_saved, "message" : message})

    
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.db import IntegrityError,transaction
from accounts.models import KitchenOwner,Renter,Chife

# Create your views here.
def register_chife(request:HttpRequest):
    msg = ""

    if request.method == "POST":
        try:

        
         with transaction.atomic():
                
                new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
                new_user.save()

                if not new_user.groups.filter(name='Chef').exists():
                    group = Group.objects.get(name="Chef")
                    new_user.groups.add(group)
                
                profile= Chife(user=new_user,about=request.POST["about"] ,avatar=request.FILES.get("avatar", KitchenOwner.avatar.field.get_default()),phone=request.POST["phone"], cv=request.FILES.get("cv"))
                profile.save()

                
         return redirect("accounts:login")
        
        except IntegrityError as e:
            msg = "This username is already taken. Please choose a different username."
            print(e)

        except Exception as e:
            msg = f"Something went wrong {e}. Please try again."
            print(e)
    

    return render(request, "chief/register_chife.html", {"msg" : msg})


def  profile_view(request:HttpRequest, user_id):
    try:
        user_object = User.objects.get(pk=user_id)
        
    except:
        return render(request, "404.html")


    return render(request, "chief/chief_profile.html", {"user_object":user_object})


def all_chief_view(request: HttpRequest):

    chife = Chife.objects.all()

    return render(request,"chief/all_chief.html", {'chife': chife})



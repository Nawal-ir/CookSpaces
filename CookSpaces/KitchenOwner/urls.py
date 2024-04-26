from django.urls import path
from . import views

app_name = "KitchenOwner"

urlpatterns  = [
 path("kitchen/Owner/Register",views.register_owner,name="register_owner"),
 path("<owner_username>/profile",views.owner_profile,name="owner_profile"),
 path("<owner_id>/add/kitchen",views.add_kitchen,name="add_kitchen"),
 path("<kitchen_id>/kitchen/details",views.kitchen_details,name="kitchen_details"),
 path("<owner_username>/update/profile",views.update_owner_profile,name="update_owner_profile"),
 path("All/kitchens",views.all_kitchens,name="all_kitchens")
  
]
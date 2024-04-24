from django.urls import path
from . import views

app_name = "KitchenOwner"

urlpatterns  = [
 path("kitchen/Owner/Register",views.register_owner,name="register_owner"),
 path("<owner_id>/add/kitchen",views.add_kitchen,name="add_kitchen")
  
]
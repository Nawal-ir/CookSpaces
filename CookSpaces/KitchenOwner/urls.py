from django.urls import path
from . import views

app_name = "KitchenOwner"

urlpatterns  = [
 path("kitchen/Owner/Register",views.register_owner,name="register_owner"),
 path("<owner_username>/profile",views.owner_profile,name="owner_profile"),
 path("add/kitchen",views.add_kitchen,name="add_kitchen"),
 path("<kitchen_id>/kitchen/details",views.kitchen_details,name="kitchen_details"),
 path("<owner_username>/update/profile",views.update_owner_profile,name="update_owner_profile"),
 path("All/kitchens/",views.all_kitchens,name="all_kitchens"),
 path("<kitchen_id>/rental/request/",views.rental_request,name="rental_request"),
 path("<owner_id>/orders/",views.owner_orders,name="owner_orders"),
 path("<order_id>/reject/order/",views.reject_order,name="reject_order"),
 path("<order_id>/accept/order/",views.accept_order,name="accept_order"),
 path("<order_id>/order/details/",views.order_details,name="order_details"),
 path("final/offer/",views.final_offer,name="final_offer"),
 path("All/kitchens/search/",views.search_cities,name="search_cities"),

  
]   
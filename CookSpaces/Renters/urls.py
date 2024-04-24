from django.urls import path
from . import views

app_name = "Renters"

urlpatterns  = [
    path("register/renter",views.register_renter, name="register_renter"),
    path("profile/",views.profile, name="profile"),
    path("order/",views.my_order, name="my_order"),
    path("booking/",views.booking, name="booking"),
    # path("favorites/<kitchen_id>",views.saved_kitchens, name="saved_kitchens"),
]
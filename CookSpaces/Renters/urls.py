from django.urls import path
from . import views

app_name = "Renters"

urlpatterns  = [
    path("register/renter",views.register_renter, name="register_renter"),
    path("renter/profile",views.profile, name="profile"),
    path("renter/order",views.my_order, name="my_order"),
    path("renter/booking",views.booking, name="booking"),
    # path("renter/<kitchen_id>/favorites",views.my_favorites, name="my_favorites"),
]
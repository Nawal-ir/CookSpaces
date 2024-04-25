from django.urls import path
from . import views

app_name = "Renters"

urlpatterns  = [
    path("register/renter",views.register_renter, name="register_renter"),
    path("profile/<user_id>/renter",views.profile, name="profile"),
    path("order/",views.my_order, name="my_order"),
    path("booking/",views.booking, name="booking"),
    path("profile/update/<user_id>",views.update_profile, name="update_profile"),
    path("saved/<kitchen_id>/kitchens",views.add_remove_saved_view, name="add_remove_saved_view"),
    path("user/saved/", views.saved_kitchens, name="saved_kitchens"),
]
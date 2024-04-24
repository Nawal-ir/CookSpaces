from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.home, name="home"),
    path("all/", views.all_kitchen, name="all_kitchen"),
    path("detail/", views.kitchen_detail, name="kitchen_detail"),
    path("delete/", views.delete_kitchen, name="delete_kitchen"),
    path("articals/", views.articals, name="articals"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("reviews/add/", views.add_review, name="add_review"),
]
from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.home, name="home"),
    path("All/", views.all_kitchen, name="all_kitchen"),
    path("Detail/", views.kitchen_detail, name="kitchen_detail"),
    path("Delete/", views.delete_kitchen, name="delete_kitchen"),
    path("Articals/", views.articals, name="articals"),
    path("About/", views.about, name="about"),
    path("Contact/", views.contact, name="contact"),
    path("reviews/add/", views.add_review, name="add_review"),
]
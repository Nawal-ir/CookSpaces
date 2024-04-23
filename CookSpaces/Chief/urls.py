from django.urls import path
from . import views

app_name = "Chief"

urlpatterns  = [
    path('profile/', views.profile_view, name='profile'),
    path("all/", views.all_chief_view, name="all_chief_view"),

]
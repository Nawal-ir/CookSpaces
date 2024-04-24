from django.urls import path
from . import views

app_name = "Chief"

urlpatterns  = [
    path('Chief/register/', views.register_chife, name='register_chife'),
    path('Chief/profile/', views.profile_view, name='profile'),
    path('Chief/all/', views.all_chief_view, name='all_chief_view'),

]
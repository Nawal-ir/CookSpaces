from django.urls import path
from . import views

app_name = "accounts"

urlpatterns  = [
    path('', views.login_user, name='login'),
    path('', views.logout_user, name='logout'),
]
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class KitchenOwner(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    commercial_register=models.FileField(upload_to="files/")
    avatar=models.FileField(upload_to="images/", default="images/profile-picture.png")
    phone=models.IntegerField()
    verified=models.BooleanField()
    def __str__(self):
        return f"{self.user.username}"


class Renter(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=models.FileField(upload_to="images/", default="")
    phone=models.IntegerField()
    about=models.TextField()
    
class Chife(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=models.FileField(upload_to="images/", default="")
    about=models.TextField()
    phone=models.IntegerField()
    cv=models.FileField()
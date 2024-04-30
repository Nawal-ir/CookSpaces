from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class KitchenOwner(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    commercial_register=models.FileField()
    avatar=models.FileField(upload_to="images/", default="images/default.jpg")
    phone=models.IntegerField()
    verified=models.BooleanField()
    
    def __str__(self):
        return f"{self.user.username}"


class Renter(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=models.FileField(upload_to="images/", default="images/default.jpg")
    phone=models.IntegerField()
    about=models.TextField()

    def __str__(self):
        return f"{self.user.username}"
    
class Chife(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=models.FileField(upload_to="images/", default="images/default.jpg")
    about=models.TextField()
    phone=models.IntegerField()
    cv=models.FileField(upload_to="images/", default="images/default.jpg")

    def __str__(self) -> str:
        return self.user.username
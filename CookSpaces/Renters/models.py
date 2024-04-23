from django.db import models
from accounts.models import KitchenOwner,Renter,kitchen
from django.core.validators import MinValueValidator, MaxValueValidator      
from django.contrib.auth.models import User


class Order(models.Model):
    status = models.TextChoices("status",["accepted","rejected", "pending","paid"])
    
    renter = models.OneToOneField()
    kitchen = models.OneToOneField()
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField()
    status = models.CharField(max_length=64,choices=status.choices)
    
class Review(models.Model):
    kitchen=models.ForeignKey(kitchen, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    evaluation = models.PositiveIntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)],null=True)

class Payment(models.Model):
    
    order = models.OneToOneField()
    name = models.CharField(max_length=2048)
    card_number = models.IntegerField()
    expired_date = models.DateField()
    cvv = models.IntegerField()

class MyFavorit(models.Model):
    
    kitchen = models.ForeignKey(kitchen, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
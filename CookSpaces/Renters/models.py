from django.db import models
from accounts.models import KitchenOwner,Renter
from KitchenOwner.models import Kitchen
from django.core.validators import MinValueValidator, MaxValueValidator      
from django.contrib.auth.models import User


class Order(models.Model):
    state = models.TextChoices("status",["مقبولة","مرفوضة", "تحت المراجعة","مدفوعة"])
    
    renter = models.ForeignKey(Renter,on_delete=models.CASCADE)
    kitchen = models.ForeignKey(Kitchen,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField()
    status = models.CharField(max_length=64,choices=state.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()


class Payment(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=2048)
    card_number = models.IntegerField()
    expired_date = models.DateField()
    cvv = models.IntegerField()

class BookMark(models.Model):
    
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
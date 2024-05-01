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
    price = models.FloatField(null=True)

    def __str__(self) -> str:
        return self.kitchen.title

class Payment(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=2048)
    card_number = models.IntegerField()
    expired_year = models.DateField(null=True)
    expired_month=models.DateField(null=True)
    cvv = models.IntegerField()

class BookMark(models.Model):
    
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.kitchen.title    
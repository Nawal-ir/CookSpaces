from django.db import models
from accounts.models import KitchenOwner
# Create your models here.

class Equipment(models.Model):
   name = models.CharField(max_length=64, unique=True)
   # add icon field and delete quantity
   icon = models.CharField(max_length=64, default="")
   
   def __str__(self):
        return self.name
    
    
class Kitchen (models.Model):    
    #choices 
    periods = models.TextChoices("period",["Monthly","Annually"])
    status_choices = models.TextChoices("status",["accepted","rejected", "pending"])
    cities = models.TextChoices("city",[('Riyadh', 'الرياض'), ('Jeddah', 'جدة'), ('Dammam', 'الدمام')])
    
    kitchen_owner = models.ForeignKey(KitchenOwner,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    desc = models.TextField()
    poster = models.ImageField(upload_to="images/")
    space = models.FloatField()
    
    has_ventilation = models.BooleanField(default=False)
    has_toilet = models.BooleanField(default=False)
    has_storage = models.BooleanField(default=False)
    has_waitingarea = models.BooleanField(default=False) 
    equipment = models.ManyToManyField(Equipment)
    loc_latitude = models.FloatField()
    loc_longitude = models.FloatField()
    price = models.FloatField()
    is_negotiable = models.BooleanField(default=False)
    city = models.CharField(max_length=100,choices=cities.choices)
    period = models.CharField(max_length=100,choices=periods.choices)
    status = models.CharField(max_length=100,choices=status_choices.choices)

    def __str__(self) -> str:
        return self.title    
    
class KitchenImage(models.Model):
    kitchen = models.ForeignKey(Kitchen,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")




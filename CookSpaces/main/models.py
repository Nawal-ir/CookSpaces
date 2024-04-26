from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator  
from KitchenOwner.models import Kitchen

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=1000)
    content = models.TextField()
    poster = models.ImageField(upload_to='poster/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username
    
class Review(models.Model):

    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    evaluation = models.PositiveIntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username
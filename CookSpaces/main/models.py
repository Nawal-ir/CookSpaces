from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator  

# Create your models here.
class Artical(models.Model):

    title = models.CharField()
    content = models.TextField()
    poster = models.ImageField(upload_to='poster/')
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    evaluation = models.PositiveIntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    created_at = models.DateTimeField(auto_now_add=True)

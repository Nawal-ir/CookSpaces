from django.contrib import admin
from .models import Article, Review, Contact
# Register your models here.

admin.site.register(Article)
admin.site.register(Review)
admin.site.register(Contact)
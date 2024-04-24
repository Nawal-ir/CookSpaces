from django.contrib import admin
from .models import Equipment,Kitchen
# Register your models here.

# class EquipmentAdmin(admin.ModelAdmin):
#     list_display=("name","quantity")
    
admin.site.register(Equipment)
admin.site.register(Kitchen)

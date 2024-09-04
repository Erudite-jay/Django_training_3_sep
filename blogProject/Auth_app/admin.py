from django.contrib import admin
from . import models 
# Register your models here.

# admin.site.register(models.Contact)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'mobile_number',"message")
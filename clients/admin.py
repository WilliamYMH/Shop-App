from django.contrib import admin
from .models import Client


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address')
    list_filter = ('name',)

# Register your models here.

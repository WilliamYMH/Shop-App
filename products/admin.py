from django.contrib import admin
from .models import Product, Favorite
# Register your models here.
# admin.site.register(Product)
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ("id", "name", "category", "description", "price")
    list_filter = ("category", "price")


@admin.register(Favorite)
class Favorite(admin.ModelAdmin):
    list_display = ('id', 'client', 'product',)

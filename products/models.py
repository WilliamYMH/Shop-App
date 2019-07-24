from django.db import models
from clients.models import Client


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)


class Favorite(models.Model):
    client = models.ForeignKey(Client, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return ('%s %s' % (self.client.name, self.product.name))

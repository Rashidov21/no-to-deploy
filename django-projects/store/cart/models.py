from django.db import models

# Create your models here.
from main.models import Product


class CardProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_products'
    )
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.product.name)


class Cart(models.Model):
    products = models.ManyToManyField(CardProduct, related_name='products')
    total_quantity = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)

    
    def __str__(self):
        return f"Cart = {self.id}"
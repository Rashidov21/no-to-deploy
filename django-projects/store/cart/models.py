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

    def add(self, product_id):
        product = Product.objects.get(id=product_id)
        self.products.create(
                product=product,
                quantity=1,
                price=product.price
            )
        self.total_quantity += 1
        self.total_price += product.price
        self.save()
        print("added")
        return True
    def __str__(self):
        return f"Cart = {self.id}"
from django.db import models
from store.models import Product
from django.contrib.auth.models import User
# Create your models here.


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

    def add(self, product_id, qty):
        product = Product.objects.get(id=product_id)
        price = product.price * qty
        self.products.create(
            product=product,
            quantity=qty,
            price=price
        )
        self.total_quantity += qty
        self.total_price += price
        self.save()
        return True

    # def deleteItem(self, product_id, qty):
    #     product = Product.objects.get(id=product_id)
    #     p_id = product.id
    #     for item in self.products.all():
    #         if item.product.id == p_id:
    #             item.delete()
    #     price = product.price * qty
    #     # self.products.remove(product)
    #     self.total_quantity -= qty
    #     self.total_price -= price
    #     self.save()
    #     return True

    def remove_all_items(self):
        self.delete()

    def __str__(self):
        return f"Cart = {self.id}"

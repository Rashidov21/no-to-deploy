from django.db import models

# Create your models here.
from shop.models import Product


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

    def add(self,product_id,qty):
        status = {}
        
        product = Product.objects.get(id=product_id)
        
        for item in self.products.all():
            print(item.product.id, "---", product.id)
           
            if item.product.id == product.id:
                status["found"] = True
            else:
                status["found"] = False
        
        if status.get("found"):
            status["done"] = False
        else:        
            price = 0
            if product.discount:            
                price = product.get_discount_price() * qty
            else:
                price = product.price * qty
            self.products.create(
                product=product,
                quantity=qty,
                price=price
            )
            self.total_quantity += qty
            self.total_price += price
            self.save()
            status["done"] = True
        return status
    def deleteItem(self, product_id,qty):
        product = Product.objects.get(id=product_id)
        for item in self.products.all():
            if item.product.id == product.id:
                item.delete()
        price = product.price * qty
        # self.products.remove(product)
        self.total_quantity -= qty
        self.total_price -= price
        self.save()
        return True
    
    def __str__(self):
        return f"Cart = {self.id}"
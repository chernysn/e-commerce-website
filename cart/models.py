from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Count, Sum


class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=500, null=False)
    price = models.FloatField(null=False)
    on_sale = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/')
    product_objects = models.Manager()

    def __str__(self):
        return f'{self.name} + {self.price}'


class AddCart(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    quantity = models.IntegerField(default='0')
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='products')
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cart_objects = models.Manager()

    def total_price_per_item(self):
        total_price_per_item = self.quantity * self.product_id.price
        return total_price_per_item

    def discount(self):
        discount = self.quantity * \
            self.product_id.price * self.product_id.on_sale / 100
        return discount

    def discounted_price(self):
        return self.quantity * self.product_id.price - self.quantity * \
            self.product_id.price * self.product_id.on_sale / 100

    def add_quantity(self, x):
        self.quantity = self.quantity + x
        return self.quantity

    def deduct_quantity(self):
        n = self.quantity - 1
        return n

    def __str__(self):
        return f'{self.product_id.name}'


class Order(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    total_to_pay = models.FloatField(default='1')
    item_id = models.ForeignKey(
        AddCart,  on_delete=models.CASCADE, related_name='items')
    order_objects = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.total_to_pay}'

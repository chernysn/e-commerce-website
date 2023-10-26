from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Count, Sum
from PIL import Image

class Category(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=500, null=False)
    category_objects = models.Manager()


class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=500, null=False)
    category_id = models.ManyToManyField(Category, related_name='categories')
    price = models.DecimalField(max_digits=100, decimal_places=2, null=False)
    on_sale = models.IntegerField(default=0,
                                  choices=[(i, i) for i in range(0, 101, 5)], null=False)
    image = models.ImageField(upload_to='uploads/')
    product_objects = models.Manager()

    def __str__(self):
        return f'{self.name} + {self.price}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image)
        width, height = img.size

        if img.width > img.height:
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.save(self.image)


    def __str__(self):
        return f'{self.name}'


class CategoryProduct(models.Model):
    category_item = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    categoryproduct_objects = models.Manager()

    def __str__(self):
        return f'{self.category_item} and {self.product_item}'


class AddCart(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    quantity = models.IntegerField(default='0')
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='products')
    client = models.CharField(max_length=100, null=False)
    cart_objects = models.Manager()

    def total_price_per_item(self):
        total_price_per_item = self.quantity * self.product_id.price
        return total_price_per_item

    def discounted_price(self):
        discounted_price = self.quantity * self.product_id.price - self.quantity * \
            self.product_id.price * self.product_id.on_sale / 100
        return discounted_price

    def add_quantity(self, x):
        self.quantity = self.quantity + x
        return self.quantity

    def deduct_quantity(self):
        return self.quantity - 1
        
    def __str__(self):
        return f'{self.product_id.name} - {self.client}'



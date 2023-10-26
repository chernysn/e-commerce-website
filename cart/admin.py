from django.contrib import admin
from .models import Product, AddCart, Category, CategoryProduct

admin.site.register(Product)
admin.site.register(AddCart)
admin.site.register(Category)
admin.site.register(CategoryProduct)


# Register your models here.

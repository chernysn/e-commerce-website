from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Product, AddCart, Category, CategoryProduct

cat_choices = Category.category_objects.all()

class CategoryForm(ModelForm):
    class Meta:
        model = Category

        fields = ['name',]
        labels = {
        }

        widgets = {
            'category': forms.Select(choices=cat_choices, attrs={'class': 'form-control form-control-sm', }),
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description',
                  'price', 'on_sale', 'image', ]
        labels = {
        }

        widgets = {
            'on_sale': forms.Select(attrs={'class': 'form-control form-control-sm', }),
        }


choices = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"),
           ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10")]


class AddCartForm(ModelForm):
    class Meta:
        model = AddCart
        fields = ['quantity']
        labels = {

        }

        widgets = {
            "quantity": forms.Select(choices=choices, attrs={'class': 'form-control form-control-sm', }),
        }



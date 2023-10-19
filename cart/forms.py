from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Product, AddCart, Order


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'price']
        labels = {

        }

        widgets = {
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


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = []
        labels = {

        }

        widgets = {
        }

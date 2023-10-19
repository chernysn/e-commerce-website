from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegistrationForm
from .forms import ProductForm, AddCartForm, OrderForm
from .models import Product, AddCart, Order
from django.db.models import Count, Sum, Q
from django.contrib.auth.models import User
from PIL import Image


def index(request):
    all_products = Product.product_objects.all()
    form = AddCartForm(request.POST)

    num_items_cart = 0

    try:
        user = request.user
        my_cart = AddCart.cart_objects.all().order_by('-id')
        my_cart = my_cart.filter(client=user)
        for item in my_cart:
            num_items_cart += item.quantity
    except:
        pass

    return render(request, 'index.html', {'form': form, 'all_products': all_products, 'num_items_cart': num_items_cart})


def add_cart(request, pr_id):

    try:
        this_product = Product.product_objects.get(id=pr_id)
        all_in_cart = AddCart.cart_objects.filter(client=request.user)
        form = AddCartForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                f = form.save(commit=False)
                for item in all_in_cart:
                    if item.product_id.id == this_product.id:
                        item_in_cart = AddCart.cart_objects.get(
                            product_id=this_product.id)
                        x = f.quantity
                        item_in_cart.add_quantity(x)
                        item_in_cart.save()
                        return redirect('cart')
                f.product_id = this_product
                f.client = request.user
                f.save()
                return redirect('index')

            else:
                form = AddCartForm()
    except:
        return redirect('cart')

    return render(request, 'index.html', {'form': form, 'this_product': this_product, })


def cart(request):

    num_items_cart = 0
    total_to_pay = 0.0

    try:
        my_cart = AddCart.cart_objects.all().order_by('-id')
        my_cart = my_cart.filter(client=request.user)
        for item in my_cart:
            num_items_cart += item.quantity

        for item in my_cart:
            if item.product_id.on_sale > 0:
                total_per_item = item.discounted_price()
                total_to_pay += total_per_item
            else:
                total_per_item = item.total_price_per_item()
                total_to_pay += total_per_item

    except:
        pass

    return render(request, 'cart.html', {'my_cart': my_cart, 'total_to_pay': total_to_pay, 'num_items_cart': num_items_cart})


def add_quantity(request, item_id):
    this_order = AddCart.cart_objects.get(id=item_id)
    if this_order is not None:
        this_order.quantity = this_order.add_quantity(1)
        this_order.total_price = this_order.total_price_per_item()
        this_order.save()
        return redirect('cart')

    return render(request, 'cart.html', {'this_order': this_order, })


def deduct_quantity(request, item_id):
    this_order = AddCart.cart_objects.get(id=item_id)
    if this_order is not None:
        this_order.quantity = this_order.deduct_quantity()
        this_order.total_price = this_order.total_price_per_item()
        this_order.save()
        if this_order.quantity <= 0:
            this_order.delete()
        return redirect('cart')

    return render(request, 'cart.html', {'this_order': this_order})


def delete_item(request, item_id):
    this_item = AddCart.cart_objects.get(id=item_id)
    if this_item is not None:
        this_item.delete()
        return redirect('cart')

    return render(request, 'cart.html', {'this_item': this_item})


def search(request):

    num_items_cart = 0
    my_cart = []
    form = AddCartForm(request.POST)

    try:
        form = AddCartForm(request.POST)
        all_products = Product.product_objects.all()

        if request.method == "POST":
            search = request.POST['search'].lower()
            search_results = Product.product_objects.filter(
                Q(name__icontains=search) | Q(description__icontains=search))

        my_cart = AddCart.cart_objects.all().order_by('-id')
        my_cart = my_cart.filter(client=request.user)
        for item in my_cart:
            num_items_cart += item.quantity

    except:
        pass

    return render(request, 'search_results.html', {'search': search, 'form': form,
                                                   'search_results': search_results, 'num_items_cart': num_items_cart, 'all_products': all_products})

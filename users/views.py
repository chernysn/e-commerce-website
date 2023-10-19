from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from cart.models import AddCart


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'user_register.html', {'form': form, })


def login_view(request):
    num_items_cart = 0
    my_cart = []
    try:
        user = request.user
        my_cart = AddCart.cart_objects.all().order_by('-id')
        my_cart = my_cart.filter(client=user)
        for item in my_cart:
            num_items_cart += item.quantity
    except:
        pass

    return render('registration/login.html', {'my_cart': my_cart, 'num_items_cart': num_items_cart})

from django.urls import path
from . import views

urlpatterns = [


    path('', views.index, name='index'),
    path('add_cart/<int:pr_id>', views.add_cart, name='add_cart'),
    path('add_quantity/<int:item_id>', views.add_quantity, name='add_quantity'),
    path('deduct_quantity/<int:item_id>',
         views.deduct_quantity, name='deduct_quantity'),
    path('delete_item/<int:item_id>',
         views.delete_item, name='delete_item'),
    path('cart', views.cart, name='cart'),
    path('search', views.search, name='search'),

]

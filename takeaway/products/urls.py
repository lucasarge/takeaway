"""This is a urls file that defines the different urls and connects the view."""

from django.urls import path
from . import views

# Used for sharing a global variable from products.
app_name = 'products'

# Declares all urls within products and links to the views.py for display.
urlpatterns = [
    path('', views.products_menu, name="menu"),
    path("cart", views.cart, name="cart"),
    path("clear_cart", views.clear_cart, name="clear_cart"),
    path("add_to_cart", views.add_to_cart, name="add"),
    path("remove_from_cart", views.remove_from_cart, name="remove"),
    path('product/<slug:slug>/', views.product_page, name="page"),
]
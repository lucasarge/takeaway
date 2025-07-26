from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_menu, name="menu"),
    path("cart", views.cart, name="cart"),
    path("add_to_cart", views.add_to_cart, name="add"),
    path("remove_from_cart", views.remove_from_cart, name="remove"),
    path('product/<slug:slug>/', views.product_page, name="page"),
]
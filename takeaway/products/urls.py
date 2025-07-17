from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_menu, name="menu"),
    path('<slug:slug>', views.product_page, name="page"),
    path("cart", views.products_cart, name="cart"),
    # path("add_to_cart", views.add_to_cart, name="add")
]
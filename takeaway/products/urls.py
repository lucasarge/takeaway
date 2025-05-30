from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_menu, name="menu"),
    path('<slug:slug>', views.product_page, name="page")
]
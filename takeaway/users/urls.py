from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

# Defining app name for users app.
app_name = 'users'

# Declares all urls within products and links to the views.py for display.
urlpatterns = [
    path('register', views.register_view, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', LogoutView.as_view(next_page="users:login"), name="logout")
]
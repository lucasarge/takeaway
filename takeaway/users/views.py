from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Users views are created below.

# register_view creates a register form and has the user POST input information.
def register_view(request):
    # If user sent POST request then check if form is valid, save and redirect.
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("products:menu")
    # Else if request is likely GET then return a new register form for user.
    else:
        form = UserCreationForm()
    # Render the html file and send dictionary with form information.
    return render(request, 'users/register.html', { "form" : form })

# login_view creates a login form and has the user POST input information.
def login_view(request):
    # If user sent POST request, check if form is valid, get info and redirect.
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("products:menu")
    # Else if request is likely GET then return a new login form for user.
    else:
        form = AuthenticationForm()
    # Render the html file and send dictionary with form information.
    return render(request, 'users/login.html', { "form" : form })
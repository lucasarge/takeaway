from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:menu")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', { "form" : form })

def login_view(request):
    return render(request, 'users/login.html')
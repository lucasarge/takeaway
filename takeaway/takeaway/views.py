# Django's function for rendering pages.
from django.shortcuts import render

def index(request):
    # This returns a render of index.html.
    return render(request, 'index.html')

def about(request):
    # This returns a render of about.html.
    return render(request, 'about.html')
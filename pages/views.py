from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    context = {
        "home_page_title": "Main",
        "description": "This is main page of my website",
    }
    return render(request, 'pages/home.html', context)

def about_page_view(request):
    context = {
        'title': 'About Us',
        'heading': 'about creatures: '
    }
    return render(request, 'pages/about.html', context)

def contact_page_view(request):
    context = {
        'item1': 123,
        'item2': 456,
        'item3': 789,
    }
    return render(request, 'pages/contact_page.html', context)

def root_page(request):
    context = {
        'name': 'ehsan',
        'age': '18',
        'major': 'computer',
    }
    return render(request, 'root.html', context)
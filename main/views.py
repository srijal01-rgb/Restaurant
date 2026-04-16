from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base(request):
    return render(request, "main/base.html")

def home(request):
     return render(request, "main/home.html")

def book(request):
     return render(request, "main/book.html")

def menu(request):
     return render(request, "main/menu.html")

def about(request):
     return render(request,"main/about.html")


    
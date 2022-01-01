from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import Product, Slider 


def projects(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'projects/projects.html', context)


def product_details(request, pk):
    proddetails = Product.objects.filter(id=pk)
    context = {'proddetails': proddetails}
    return render(request, 'projects/product_details.html', context)


def home(request):
    sliders = Slider.objects.all()
    context = {'sliders':sliders}
    return render(request, 'projects/home.html', context)


def about(request):
    return render(request, 'projects/about.html')


def contact(request):
    return render(request, 'projects/contact.html')
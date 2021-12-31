from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import Product 


def projects(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'projects/projects.html', context)


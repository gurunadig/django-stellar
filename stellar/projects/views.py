from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import Product, Category 
from django.contrib import messages

def projects(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    context = {'products':products, 'categorys':categorys}
    return render(request, 'projects/projects.html', context)


def product_details(request, pk):
    proddetails = Product.objects.filter(id=pk)
    context = {'proddetails': proddetails}
    return render(request, 'projects/product_details.html', context)


def home(request):

    return render(request, 'projects/home.html')


def about(request):
    return render(request, 'projects/about.html')


def contact(request):
    return render(request, 'projects/contact.html')  


def category(request, pk):
    categorys = Category.objects.all()
    if(Category.objects.filter(id=pk)):
        products = Product.objects.filter(category__id=pk)
        category_details = Category.objects.filter(id=pk)
        context = {'products': products, 'category_details':category_details, 'categorys':categorys}
        return render(request, 'projects/category.html', context)  
    else:
        messages.warning(request, "No Such Category Found !")
        return render('category')


from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import Product, Category, Catalog 
from django.contrib import messages
from .filters import ProductFilter


def projects(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    context = {'products':products, 'categorys':categorys, 'myFilter':myFilter}
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
        myFilter = ProductFilter(request.GET, queryset=products)
        products = myFilter.qs
        context = {'products': products, 'category_details':category_details, 'categorys':categorys, 'myFilter':myFilter}
        return render(request, 'projects/category.html', context)  
    else:
        messages.warning(request, "No Such Category Found !")
        return render('category')



def services(request):
    return render(request, 'projects/services.html')  


def catalog(request):
    catalogs = Catalog.objects.all()
    context = {'catalogs':catalogs}
    return render(request, 'projects/catalog.html', context)  
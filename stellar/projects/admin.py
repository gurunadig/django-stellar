from django.contrib import admin
from .models import  Product, Category, Product_category, Catalog


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Product_category)
admin.site.register(Catalog)

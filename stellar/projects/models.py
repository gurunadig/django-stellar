from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(default="400-200.png", null=False, blank=True)
    product_category = models.ForeignKey('Product_category', null=False, blank=False, on_delete=models.CASCADE)
    product_description = models.TextField(blank=False, null=False)
    product_technical_specs = models.TextField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    product_tag = models.CharField(max_length=50, blank=False, null=False)
    category = models.ForeignKey('Category', null=False, blank=False, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Product_category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name




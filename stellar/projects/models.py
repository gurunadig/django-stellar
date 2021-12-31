from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    product_name = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(null=True, blank=True)
    product_category = models.CharField(max_length=100, blank=False, null=False)
    product_subcategory = models.CharField(max_length=100, blank=False, null=False)
    product_description = models.TextField(blank=False, null=False)
    product_technical_specs = models.TextField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    product_tag = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.product_name



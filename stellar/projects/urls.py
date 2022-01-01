from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('product_details/<str:pk>', views.product_details, name='product_details'),
]

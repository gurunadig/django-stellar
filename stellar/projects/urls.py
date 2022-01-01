from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('product_details/<str:pk>', views.product_details, name='product_details'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

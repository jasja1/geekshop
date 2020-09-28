from django.urls import path
from django.contrib import admin
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', mainapp.products, name='products'),
    path('products/all/', mainapp.products, name='products_all'),
    path('products/home/', mainapp.products, name='products_home'),
    path('products/modern/', mainapp.products, name='products_modern'),
    path('products/office/', mainapp.products, name='products_office'),
    path('products/classic/', mainapp.products, name='products_classic'),
    path('contact/', mainapp.contact, name='contact'),
    path('admin/', admin.site.urls),
]
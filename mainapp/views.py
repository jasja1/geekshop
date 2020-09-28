from django.shortcuts import render

from mainapp.models import Product, ProductCategory, Contact


def main(request):
    title = 'продукты'
    products = Product.objects.all()[:3]
    context = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    title = 'продукты'
    context = {
        'title': title,
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    contacts = Contact.objects.all()
    title = 'контакты'
    context = {
        'title': title,
        'contacts': contacts
    }
    return render(request, 'mainapp/contact.html', context)

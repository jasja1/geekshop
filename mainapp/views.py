from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory, Contact


def main(request):
    title = 'главная'
    products = Product.objects.all()[:3]
    context = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).values_list('quantity', flat=True)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('-price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', context)

    same_product = Product.objects.all()[3:5]
    context = {
        'title': title,
        'links_menu': links_menu,
        'same_product': same_product,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    title = 'контакты'
    contacts = Contact.objects.all()
    context = {
        'title': title,
        'contacts': contacts
    }
    return render(request, 'mainapp/contact.html', context)

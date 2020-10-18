from random import sample

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory, Contact


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.filter(is_active=True)

    return sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category, is_active=True). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    title = 'главная'
    products = Product.objects.filter(is_active=True)[:3]
    context = {
        'title': title,
        'products': products,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None, page=1, items_counts=2):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.objects.filter(is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True).order_by('-price')

        paginator = Paginator(products, items_counts)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'basket': get_basket(request.user),
        }

        return render(request, 'mainapp/products_list.html', context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
        'basket': get_basket(request.user),

    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    title = 'контакты'
    contacts = Contact.objects.all()
    context = {
        'title': title,
        'contacts': contacts,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', context)


def product(request, pk):
    product_item = get_object_or_404(Product, pk=pk)

    content = {
        'title': product_item.name,
        'links_menu': ProductCategory.objects.all(),
        'product': product_item,
        'basket': get_basket(request.user),
        'same_products': get_same_products(product_item)
    }

    return render(request, 'mainapp/product.html', content)

from django.conf import settings
from django.shortcuts import render
import json
import os


def main(request):
    title = 'продукты'
    context = {
        'title': title
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    try:
        with open(os.path.join(settings.BASE_DIR, "links_menu.json")) as json_file:
            links_menu = json.load(json_file)
    except IOError:
        links_menu = [
            {'href': 'products_all', 'name': 'все'},
            {'href': 'products_home', 'name': 'дом'},
            {'href': 'products_office', 'name': 'офис'},
            {'href': 'products_modern', 'name': 'модерн'},
            {'href': 'products_classic', 'name': 'классика'},
        ]
    title = 'продукты'
    context = {
        'title': title,
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    title = 'контакты'
    context = {
        'title': title
    }
    return render(request, 'mainapp/contact.html', context)

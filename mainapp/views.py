from django.shortcuts import render
import json

try:
    with open("links_menu1.json", "r") as read_file:
        links_menu = json.load(read_file)
except IOError:
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]


def main(request):
    title = 'продукты'
    context = {
        'title': title
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
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

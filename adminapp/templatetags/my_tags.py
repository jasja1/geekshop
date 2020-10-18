from django import template

from geekshop import settings

register = template.Library()


def media_folder_products(string):
    if not string:
        string = 'products_images/defaults.jpg'

    return f'{settings.MEDIA_URL}{string}'


register.filter('media_folder_products', media_folder_products)


@register.filter(name='media_folder_users')
def media_folder_users(string):
    if not string:
        string = 'users_avatars/defaults.jpg'

    return f'{settings.MEDIA_URL}{string}'

import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product, Contact

FILE_PATH = os.path.join(settings.BASE_DIR, 'mainapp/json')


def load_from_json(file_name):
    with open(os.path.join(FILE_PATH, file_name + ".json"), encoding='utf-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            Product.objects.create(**product)

        contacts = load_from_json('contacts')

        Contact.objects.all().delete()
        for contact in contacts:
            Contact.objects.create(**contact)

        # Создаем суперпользователя при помощи менеджера модели
        ShopUser.objects.all().delete()
        super_user = ShopUser.objects.create_superuser('django',
                                                       'django@geekshop.local',
                                                       'geekbrains',
                                                       age=33,
                                                       avatar='users_avatars/icon-hover.png')

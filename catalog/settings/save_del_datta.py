from django.core.management import BaseCommand

from catalog.models import Category

'''Удаление и сохранения данных'''


class Job(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()

        # Очищение БД

        categories = [
            {'category_name': '', 'description': ''},
            {'category_name': '', 'description': ''}
        ]

        # Данные для записи

        data = []
        for category in categories:
            data.append(Category(**category))

        # Сохранение БД
        Category.objects.bulk_create(data)

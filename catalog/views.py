from django.shortcuts import render

from catalog.models import Product


def contacts(request):
    context = {
        'title_contacts': 'SlyStore - Контакты',
    }
    return render(request, 'catalog/contacts.html', context)


def index(request):
    context = {
        'object_list': Product.objects.all()[:100],
        'title': 'SlyStore - Домашняя страница',
    }
    return render(request, 'catalog/index.html', context)

def collection(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'SlyStore - Каталог',
    }
    return render(request, 'catalog/collection.html', context)

def product_id(request, id):
    category_item = Product.objects.get(id=id)
    context = {
        'object': Product.objects.filter(category_item=id),
        'product': f'Продукт{category_item.name_prod}',
    }
    return render(request, 'catalog/prod.html', context)


from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    objects = None
    category_name = models.CharField(max_length=250, verbose_name='Категория продукта')
    information = models.TextField(max_length=250, verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)
#




class Product(models.Model):
    product_name = models.CharField(max_length=250, verbose_name='Наименование')
    information = models.TextField(max_length=250, verbose_name='Описание')
    imagef = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.PositiveIntegerField(verbose_name='Цена за покупку')
    date_creation = models.DateTimeField(max_length=250, verbose_name='Дата создания')
    date_change = models.DateTimeField(max_length=250, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)

#
#
#





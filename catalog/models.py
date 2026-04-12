from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание продукта')
    product_image = models.ImageField(verbose_name='Изображение продукта')
    category = models.CharField(max_length=100, verbose_name='Наименование категории продукта')
    price = models.FloatField(verbose_name='Цена продукта')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.product_name}, {self.category}, {self.price}, {self.created_at}, {self.updated_at}'

class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание категории')
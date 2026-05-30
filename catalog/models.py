from django.db import models
from django.conf import settings
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание категории")

    def __str__(self):
        return f"{self.name}, {self.description}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание продукта")
    image = models.ImageField(verbose_name="Изображение продукта")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.FloatField(verbose_name="Цена продукта")
    created_at = models.DateField(verbose_name="Дата создания")
    updated_at = models.DateField(verbose_name="Дата последнего изменения")
    is_published = models.BooleanField(verbose_name="Опубликовано", default=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец"
    )

    def __str__(self):
        return f"{self.name}, {self.category}, {self.price}, {self.created_at}, {self.updated_at}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
        ]
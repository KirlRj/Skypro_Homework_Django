from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(upload_to="blog/", verbose_name="Изображение")
    created_at = models.DateTimeField(verbose_name="Дата создания")
    is_published = models.BooleanField(verbose_name="Опубликовано", default=False)
    views_count = models.PositiveIntegerField(verbose_name="Количество просмотров", default=0)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "ББлоги"

    def __str__(self):
        return f"{self.title}, {self.created_at}, {self.is_published}, {self.views_count}"

    def increment_views(self):
        self.views_count += 1
        self.save(update_fields=["views_count"])

from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "is_published", "views_count", "created_at"]
    list_filter = ["is_published", "created_at"]
    search_fields = ["title", "content"]
    list_editable = ["is_published"]
    readonly_fields = ["views_count"]

    fieldsets = (
        ("Основная информация", {"fields": ("title", "content", "image")}),
        ("Публикация", {"fields": ("is_published", "created_at")}),
        ("Статистика", {"fields": ("views_count",)}),
    )

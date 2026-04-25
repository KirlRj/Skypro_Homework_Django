from datetime import date

from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавляет тестовые продукты"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Старые продукты удалены"))

        try:
            smartphones = Category.objects.get(name="Смартфоны")
            laptops = Category.objects.get(name="Ноутбуки")
            tablets = Category.objects.get(name="Планшеты")
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR("Категории не найдены! Сначала создайте категории."))
            return

        today = date.today()

        products = [
            {
                "name": "iPhone 15 Pro",
                "description": "Смартфон Apple",
                "image": "products/iphone.jpg",
                "category": smartphones,
                "price": 99900,
                "created_at": today,
                "updated_at": today,
            },
            {
                "name": "Samsung Galaxy S24",
                "description": "Смартфон Samsung",
                "image": "products/samsung.jpg",
                "category": smartphones,
                "price": 89900,
                "created_at": today,
                "updated_at": today,
            },
            {
                "name": "MacBook Pro 14",
                "description": "Ноутбук Apple",
                "image": "products/macbook.jpg",
                "category": laptops,
                "price": 199900,
                "created_at": today,
                "updated_at": today,
            },
            {
                "name": "iPad Pro",
                "description": "Планшет Apple",
                "image": "products/ipad.jpg",
                "category": tablets,
                "price": 109900,
                "created_at": today,
                "updated_at": today,
            },
            {
                "name": "Xiaomi 14",
                "description": "Смартфон Xiaomi",
                "image": "products/xiaomi.jpg",
                "category": smartphones,
                "price": 49900,
                "created_at": today,
                "updated_at": today,
            },
        ]

        for p in products:
            Product.objects.create(**p)

        self.stdout.write(self.style.SUCCESS(f"Новые продукты добавлены! Всего: {len(products)}"))

from catalog.models import Product
from django.core.cache import cache

def get_products_by_category(category_id):
    """Возвращает список продуктов в указанной категории с кэшированием"""
    cache_key = f'product_by_category_{category_id}'

    products = cache.get(cache_key)

    if products is None:
        products = list(Product.objects.filter(
            category_id=category_id
        ).select_related('category'))
        cache.set(cache_key, products, 60)

    return products
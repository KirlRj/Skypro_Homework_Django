from django.urls import path
from catalog import views
from django.views.decorators.cache import cache_page
app_name = "catalog"

urlpatterns = [
    path("", views.HomeListView.as_view(), name="home"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", cache_page(60)(views.ProductDetailView.as_view()), name="product_detail"),
    path("product/create/", views.ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", views.ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path('product/<int:pk>/unpublish/', views.product_unpublish, name='product_unpublish'),
    path("category/<int:category_id>/", views.ProductsByCategory.as_view(), name="product_by_category"),
]
from django.urls import path

from catalog.views import ContactsView, HomeListView, ProductDetailView

app_name = "catalog"

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]

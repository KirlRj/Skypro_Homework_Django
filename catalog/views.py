from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import permission_required

from catalog.models import Product
from catalog.forms import ProductForm


class HomeListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.select_related("category").all()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = "pk"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавить продукт"
        return context

    def form_valid(self, form):
        """Автоматическая привязка продукта к текущему пользователю"""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактировать продукт"
        return context


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")
    permission_required = "catalog.delete_product"

    def test_func(self):
        # владелец или модератор может удалять
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm('catalog.delete_product')


@permission_required('catalog.can_unpublish_product')
def product_unpublish(request, pk):
    """Снятие продукта с публикации"""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.is_published = False
        product.save()
    return redirect('catalog:product_detail', pk=pk)


class ContactsView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Сообщение от {name} ({phone}): {message}")
        context = self.get_context_data(**kwargs)
        context["message"] = "Спасибо за обращение! Мы свяжемся с вами."
        return self.render_to_response(context)

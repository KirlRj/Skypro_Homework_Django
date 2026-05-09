from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product

# def home(request):
#     products = Product.objects.select_related('category').all()
#     context = {'products': products,}
#     return render(request, "home.html",context)


class HomeListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.select_related("category").all()


# def product_detail(request, pk):
#
#     product = get_object_or_404(Product, id=pk)
#
#     context = {
#         'product': product,
#     }
#     return render(request, 'product_detail.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = "pk"


# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         print(f"Сообщение от {name} ({phone}): {message}")
#         return render(request, "contacts.html", {"message": "Спасибо за обращение! Мы свяжемся с вами."})
#     return render(request, "contacts.html")


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

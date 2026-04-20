from django.shortcuts import render,  get_object_or_404
from catalog.models import Product


def home(request):
    products = Product.objects.select_related('category').all()
    context = {'products': products,}
    return render(request, "home.html",context)

def product_detail(request, pk):

    product = get_object_or_404(Product, id=pk)

    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Сообщение от {name} ({phone}): {message}")
        return render(request, "contacts.html", {"message": "Спасибо за обращение! Мы свяжемся с вами."})
    return render(request, "contacts.html")

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Сообщение от {name} ({phone}): {message}")
        return render(request, 'contacts.html', {
            'message': 'Спасибо за обращение! Мы свяжемся с вами.'
        })
    return render(request, 'contacts.html')
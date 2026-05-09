from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта',
    'биржа', 'дешево', 'бесплатно',
    'обман', 'полиция', 'радар',
]


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Название продукта'
        self.fields['description'].widget.attrs['placeholder'] = 'Описание продукта'
        self.fields['price'].widget.attrs['placeholder'] = 'Цена в рублях'

    def _check_forbidden_words(self, value, field_label):
        value_lower = value.lower()
        for word in FORBIDDEN_WORDS:
            if word in value_lower:
                raise forms.ValidationError(
                    f'Поле «{field_label}» содержит запрещённое слово: «{word}».'
                )
        return value

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        return self._check_forbidden_words(name, 'Название')

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        return self._check_forbidden_words(description, 'Описание')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError('Цена продукта не может быть отрицательной.')
        return price
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
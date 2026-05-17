from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    """Форма регистрации пользователя"""

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "avatar", "phone", "country")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"

    def clean_email(self):
        """Проверка на уникальность email в БД"""
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует!")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if phone:
            if phone.isdigit():
                if phone[0] != "7":
                    raise forms.ValidationError("Номер телефона должен начинаться с 7!")
                elif len(phone) != 11:
                    raise forms.ValidationError("Номер телефона должен иметь 11 цифр!")
                else:
                    return phone
            else:
                raise forms.ValidationError("Поле телефон может состоять только из цифр!")
        return phone


class UserLoginForm(AuthenticationForm):
    """Форма аутентификации пользователя"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

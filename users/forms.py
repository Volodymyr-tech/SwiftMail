from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import CustomUser


class StyleProductMixin:
    '''Миксин для стилизации полей формы'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{existing_classes} form-control".strip()


class CustomUserCreationForm(StyleProductMixin, UserCreationForm):
    '''Форма для регистрации нового юзера'''
    username = forms.CharField(max_length=50, required=True)

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
            "phone_number",
            "password1",
            "password2",
            "avatar",
            "country",
        )


    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        return phone_number


class UserEditForm(StyleProductMixin, forms.ModelForm):
    '''Форма для изменения профиля юзера'''
    class Meta:
        model = CustomUser
        fields = ("email", "phone_number", "avatar")


class UserLoginForm(StyleProductMixin, AuthenticationForm):
    '''Форма для входа зарегистрированного юзера'''
    pass


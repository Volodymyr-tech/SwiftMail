from django import forms

from clients.models import Client
from utils.mixins import StyleProductMixin


class ClientForm(StyleProductMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'  # Теперь Django знает, какие поля использовать

from django import forms

from clients.models import Client
from utils.mixins import StyleProductMixin


class ClientForm(StyleProductMixin, forms.ModelForm):
    model = Client
    fields = '__all__'

from django import forms

from message.models import Message
from utils.mixins import StyleProductMixin


class CreateMessageForm(StyleProductMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'  # Теперь Django знает, какие поля использовать
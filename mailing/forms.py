from django import forms

from mailing.models import Mail
from utils.mixins import StyleProductMixin


class MailForm(StyleProductMixin, forms.ModelForm):
    class Meta:
        model = Mail
        fields = ["message", "client",]
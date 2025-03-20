from django.db import models
from django.utils.text import slugify

from users.models import CustomUser


# Create your models here.
class Client(models.Model):
    email = models.EmailField(unique=True, max_length=55)
    name = models.CharField(max_length=155) #Можно разделить на 3 поля или last name first name
    comment = models.CharField(max_length=255)
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="clients",
        verbose_name="Creator of the recipient", blank=True, null=True)


    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['name']
from django.db import models

# Create your models here.
class Client(models.Model):
    email = models.CharField(primary_key=True, max_length=55)
    name = models.CharField(max_length=155) #Можно разделить на 3 поля или last name first name
    comment = models.CharField(max_length=255)



    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['name']
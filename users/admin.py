from django.contrib import admin

from users.models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'country')
    search_fields = ('username', 'email')
    list_filter = ("is_active", "is_staff")
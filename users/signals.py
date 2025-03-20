from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from users.models import CustomUser
from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
@receiver(post_delete, sender=CustomUser)
def clear_mailing_custom_user(sender, instance, **kwargs):
    # Очищаем кэш для списка продуктов зарегистрированых и не зарегистрированых юзеров
    cache.delete("cache_all_custom_users")
    print("🚀 Cache is empty!")
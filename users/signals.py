from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from users.models import CustomUser
from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
@receiver(post_delete, sender=CustomUser)
def clear_mailing_custom_user(sender, instance, **kwargs):
    # Очищаем кэш для списка продуктов зарегистрированых и не зарегистрированых юзеров
    cache.delete("cache_all_messages")

    # ❗ Удаляем кэш списка для каждого user_id
    for user_id in CustomUser.objects.values_list("id", flat=True):
            cache.delete(f"cache_messages_{user_id}")

    print("🚀 Cache is empty!")
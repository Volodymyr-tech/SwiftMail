from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from mailing.models import Mail
from users.models import CustomUser


@receiver(post_save, sender=Mail)
@receiver(post_delete, sender=Mail)
def clear_mailing_cache(sender, instance, **kwargs):
    # Очищаем кэш для списка продуктов зарегистрированых и не зарегистрированых юзеров
    cache.delete("cache_all_mails")

    # ❗ Удаляем кэш списка для каждого user_id
    for user_id in CustomUser.objects.values_list("id", flat=True):
            cache.delete(f"cache_mails_{user_id}")

    print("🚀 Cache is empty!")
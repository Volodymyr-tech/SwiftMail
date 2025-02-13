from users.models import CustomUser
from config.settings import CACHE_ENABLED
from django.core.cache import cache


class CacheAllCustomUsers:
    @staticmethod
    def get_cache_all_custom_users():
        if CACHE_ENABLED:
            #user_id = request.user.id
            cache_key = f'cache_all_custom_users'
            cache_messages = cache.get(cache_key)

            if cache_messages is None:
                queryset = CustomUser.objects.all()
                cache.set(cache_key, queryset, 60 * 60)  # Cache for 1 hour
                return queryset

            return cache_messages
        else:
            return CustomUser.objects.all()


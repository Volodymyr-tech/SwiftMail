from message.models import Message
from config.settings import CACHE_ENABLED
from django.core.cache import cache


class CacheMessage:
    @staticmethod
    def get_cache_user_messages(request):
        if CACHE_ENABLED:
            user_id = request.user.id
            cache_key = f'cache_messages_{user_id}'
            cache_messages = cache.get(cache_key)

            if cache_messages is None:
                queryset = Message.objects.filter(owner=request.user)
                cache.set(cache_key, queryset, 60 * 60)  # Cache for 1 hour
                return queryset

            return cache_messages
        else:
            return Message.objects.filter(owner=request.user)


    @staticmethod
    def get_all_messages():
        if CACHE_ENABLED:
            cache_key = 'cache_all_messages'
            cache_messages = cache.get(cache_key)

            if cache_messages is None:
                queryset = Message.objects.all()
                cache.set(cache_key, queryset, 60 * 60)  # Cache for 1 hour
                return queryset

            return cache_messages

        else:
            return Message.objects.all()
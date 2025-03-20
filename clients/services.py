from clients.models import Client
from config.settings import CACHE_ENABLED
from django.core.cache import cache


class CacheClients:
    @staticmethod
    def get_cache_user_clients(request):
        if CACHE_ENABLED:
            user_id = request.user.id
            cache_key = f'cache_clients_{user_id}'
            cache_clients = cache.get(cache_key)

            if cache_clients is None:
                queryset = Client.objects.filter(owner=request.user)
                cache.set(cache_key, queryset, 60 * 60)  # Cache for 1 hour
                return queryset

            return cache_clients
        else:
            return Client.objects.filter(owner=request.user)


    @staticmethod
    def get_all_clients():
        if CACHE_ENABLED:
            cache_key = 'cache_all_clients'
            cache_clients = cache.get(cache_key)

            if cache_clients is None:
                queryset = Client.objects.all()
                cache.set(cache_key, queryset, 60 * 60)  # Cache for 1 hour
                return queryset

            return cache_clients

        else:
            return Client.objects.all()
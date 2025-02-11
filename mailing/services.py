from mailing.models import Mail, MailingAttempt
from config.settings import CACHE_ENABLED
from django.core.cache import cache


class CacheMailing:
    @staticmethod
    def get_cache_user_mails(request):
        if CACHE_ENABLED:
            user_id = request.user.id
            cache_key = f'cache_mails_{user_id}'
            cache_clients = cache.get(cache_key)

            if cache_clients is None:
                queryset = Mail.objects.filter(owner=request.user)
                cache.set(cache_key, queryset, 60 * 60)  # Cache for 1 hour
                return queryset

            return cache_clients
        else:
            return Mail.objects.filter(owner=request.user)


    @staticmethod
    def get_all_mails():
        if CACHE_ENABLED:
            cache_key = 'cache_all_mails'
            cache_clients = cache.get(cache_key)

            if cache_clients is None:
                queryset = Mail.objects.all()
                cache.set(cache_key, queryset, 60 * 60)  # Cache for 1 hour
                return queryset

            return cache_clients

        else:
            return Mail.objects.all()
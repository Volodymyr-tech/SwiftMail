from django.core.cache import cache
from django.http import HttpRequest
from django.apps import apps
from config.settings import CACHE_ENABLED


class CacheService:
    @staticmethod
    def get_cached_obj_or_objects(app_name: str, model_name: str, object_id=None, request: HttpRequest = None):
        """Получает кэшированную страницу или объект только для пользователя с совпадающим sessionid или user_id"""
        if CACHE_ENABLED:
            #session_id = request.COOKIES.get("sessionid") if request.COOKIES.get("sessionid") else "non_registered_user"# Получаем sessionid из Cookies
            #print(session_id)
            user_id = request.user.id if request.user.is_authenticated else "Guest"  # Получаем ID пользователя

            # ❗ Разделяем кэш для списка и детального просмотра
            if object_id:
                cache_key = f"{model_name}_detail_{object_id}_{user_id}"  # Уникальный ключ для одного объекта
            else:
                cache_key = f"{model_name}_list_{user_id}"  # Уникальный ключ для списка

            # Проверяем, есть ли данные в кэше
            cached_data = cache.get(cache_key)
            if cached_data:
                print(f"Отдаем кэшированные данные для {cache_key}")
                return cached_data  # Если данные найдены в кэше, возвращаем их

            # Загружаем модель
            model = apps.get_model(app_name, model_name)
            print(f"Данных нет в кэше, загружаем из базы... {model}")

            # Загружаем объект или QuerySet
            obj = model.objects.get(id=object_id) if object_id else model.objects.all()


            # Сохраняем в кэш
            cache.set(cache_key, obj, timeout=60*10)  # Кэшируем на 1 час
            return obj  # Возвращаем объект
        else:
            print("Кэширование отключено")
            model = apps.get_model(app_name, model_name)
            obj = model.objects.get(id=object_id) if object_id else model.objects.all()
            return obj  # Возвращаем объект



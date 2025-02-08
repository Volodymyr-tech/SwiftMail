from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        try:
            # Укажите имя пользователя или email суперюзера, которого нужно удалить
            admin_user = User.objects.get(
                username="supermanager"
            )  # Используйте уникальное поле
            admin_user.delete()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Администратор успешно удалён: {admin_user.username}"
                )
            )
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Суперюзер с таким именем не найден."))

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="supermanager1",
            email="vovateslenko.1996.28@gmail.com",
            first_name="Vova",
            last_name="Teslenko",
        )
        admin_user.set_password("PswqPwfsqWF2212")

        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()

        self.stdout.write(
            self.style.SUCCESS(f"Администратор успешно создан: {admin_user.email}")
        )

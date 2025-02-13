from django.contrib.auth.models import User, Group

class UserService:
    @staticmethod
    def assign_service_user(user):
        """
        Добавляет пользователя в группу 'Service Users'.
        :param user: Экземпляр пользователя, которому нужно назначить группу.
        """
        group, created = Group.objects.get_or_create(name="Service Users")

        if not user.groups.filter(name="Service Users").exists():
            user.groups.add(group)
            user.save()
            return f"User {user.username} was added to 'Service Users'"
        return f"User {user.username} already in 'Service Users'"

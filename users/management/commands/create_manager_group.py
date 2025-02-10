from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Creates a group called 'Managers' and assigns permissions to it"

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Managers")

        try:
            view_client = Permission.objects.get(codename="view_client")
            view_mail = Permission.objects.get(codename="view_mail")
            change_mail = Permission.objects.get(codename="change_mail")
            change_customuser = Permission.objects.get(codename="change_customuser")
            view_customuser = Permission.objects.get(codename="view_customuser")


            group.permissions.add()

            if created:
                self.stdout.write(self.style.SUCCESS("The 'Managers' group has been successfully created"))
            else:
                self.stdout.write(self.style.WARNING("The Managers group already exists"))

        except Permission.DoesNotExist as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))

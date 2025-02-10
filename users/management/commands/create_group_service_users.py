from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Creates a group called 'Service Users' and assigns permissions to it"

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Service Users")

        try:
            view_client = Permission.objects.get(codename="view_client")
            add_client = Permission.objects.get(codename="add_client")
            change_client = Permission.objects.get(codename="change_client")
            delete_client = Permission.objects.get(codename="delete_client")

            view_mail = Permission.objects.get(codename="view_mail")
            change_mail = Permission.objects.get(codename="change_mail")
            add_mail = Permission.objects.get(codename="add_mail")
            delete_mail = Permission.objects.get(codename="delete_mail")

            view_message = Permission.objects.get(codename="view_message")
            change_message = Permission.objects.get(codename="change_message")
            add_message = Permission.objects.get(codename="add_message")
            delete_message = Permission.objects.get(codename="delete_message")


            view_mailingattempt = Permission.objects.get(codename="view_mailingattempt")


            group.permissions.add(view_client, add_client, change_client, delete_client,
                                  view_mail, change_mail, add_mail, delete_mail,
                                  view_message, add_message, change_message, delete_message)

            if created:
                self.stdout.write(self.style.SUCCESS("The 'Service Users' group has been successfully created"))
            else:
                self.stdout.write(self.style.WARNING("The 'Service Users' group already exists"))

        except Permission.DoesNotExist as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))

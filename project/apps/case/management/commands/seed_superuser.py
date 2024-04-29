from django.core.management.base import BaseCommand

from project.apps.users.models import User


class Command(BaseCommand):
    help = "Seed with super user"

    def handle(self, *args, **options):
        # Check if a superuser with the username "admin" already exists
        superuser = User.objects.filter(username="admin", is_superuser=True).first()

        if superuser:
            self.stdout.write(self.style.SUCCESS('There is a Superuser "admin" with a password.'))
        else:
            # Create a new superuser
            user = User.objects.create_superuser(
                username="admin",
                email="admin@admin.dk",
                password="password",
                first_name="Ole",
                last_name="Thestrup",
            )
            self.stdout.write(
                self.style.SUCCESS('Shhh!!!! Superuser created successfully with username "admin" and password "pass".')
            )

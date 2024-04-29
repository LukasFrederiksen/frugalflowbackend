from django.core.management.base import BaseCommand

from faker import Faker

from project.apps.users.models import User


class Command(BaseCommand):
    help = 'Database seed users with fake data'

    def handle(self, *args, **options):

        if User.objects.count() < 2:

            fake = Faker()

            for _ in range(10):
                username = fake.user_name()
                email = fake.email()
                password = fake.password()
                first_name = fake.first_name()
                last_name = fake.last_name()

                User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            self.stdout.write(self.style.SUCCESS('10 Users have been seeded to the database.'))

        else:
            self.stdout.write(self.style.SUCCESS('The database already contains users. No seeding required.'))

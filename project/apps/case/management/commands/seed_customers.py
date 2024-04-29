from django.core.management.base import BaseCommand
from faker import Faker
from project.apps.customer.models import Customer


class Command(BaseCommand):
    help = "Database seed customers with fake data"

    def handle(self, *args, **options):
        fake = Faker()

        # Check if there are already customers in the database
        if Customer.objects.exists():
            self.stdout.write(
                self.style.SUCCESS("Customers already exist. No seeding required.")
            )
        else:
            for _ in range(10):
                name = fake.name()
                description = fake.text()
                email = fake.email()
                phone = fake.phone_number()
                phone = phone[:10]
                address = fake.address()
                customer_picture = 'https://frugal.dk/wp-content/uploads/2022/02/fugal-white-logo.png'

                Customer.objects.create(
                    name=name,
                    description=description,
                    email=email,
                    phone=phone,
                    address=address,
                    customer_picture=customer_picture
                )
                self.stdout.write(self.style.SUCCESS("Customer created successfully."))

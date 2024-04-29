import random
from django.core.management.base import BaseCommand
from faker import Faker
from project.apps.vessel.models import Vessel


class Command(BaseCommand):
    help = "Database seed vessel with fake data"

    def handle(self, *args, **options):
        fake = Faker()

        # Check if there are already vessels in the database
        if Vessel.objects.exists():
            self.stdout.write(
                self.style.SUCCESS("Vessels already exist. No seeding required.")
            )
        else:
            for _ in range(30):
                name = fake.last_name()
                imo = random.randint(1000000, 9999999)
                type = random.choice(Vessel.VESSEL_TYPE_CHOICES)[1]

                Vessel.objects.create(
                    name=name,
                    imo=imo,
                    type=type,
                )
                self.stdout.write(self.style.SUCCESS("Vessel created successfully."))

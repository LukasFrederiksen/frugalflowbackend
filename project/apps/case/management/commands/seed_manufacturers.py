from django.core.management.base import BaseCommand
from faker import Faker
from project.apps.manufacture.models import Manufacture


class Command(BaseCommand):
    help = "Database seed manufacturers with fake data"

    def handle(self, *args, **options):
        fake = Faker()

        # Check if there are already manufactures in the database
        if Manufacture.objects.exists():
            self.stdout.write(
                self.style.SUCCESS("Manufacturers already exist. No seeding required.")
            )
        else:
            for _ in range(20):
                cvr = fake.random_int(min=1,max=99999999)
                name = fake.name()
                contactperson = fake.name()
                phone = fake.phone_number()
                phone = phone[:10]
                email = fake.email()
                website = 'www.landbrugsavisen.dk'
                picture_logo = 'https://frugal.dk/wp-content/uploads/2022/02/fugal-white-logo.png'
                
                
                Manufacture.objects.create(
                    cvr=cvr,
                    name=name,
                    contactperson=contactperson,
                    email=email,
                    phone=phone,
                    website=website, 
                    picture_logo=picture_logo,
                    
                )
                self.stdout.write(self.style.SUCCESS("Manufacture created successfully."))

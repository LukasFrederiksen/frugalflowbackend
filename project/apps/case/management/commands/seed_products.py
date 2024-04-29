import random
from django.core.management.base import BaseCommand
from faker import Faker
from project.apps.manufacture.models import Manufacture
from project.apps.product.models import Product


class Command(BaseCommand):
    help = "Database seed product with fake data"

    def handle(self, *args, **options):
        fake = Faker()

        def generate_sku():
            letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
            numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
            return f'{letters}{numbers}'

        # Check if there are already products in the database
        if Product.objects.exists():
            self.stdout.write(
                self.style.SUCCESS("Products already exist. No seeding required.")
            )
        else:
            manufactures = list(Manufacture.objects.all())
            for _ in range(20):
                serial_number = random.randint(100000, 900000)
                name = fake.name()
                sku = generate_sku()
                qty = random.randint(1, 300)
                description = fake.text(50)
                cost_price = random.randint(100, 10000)
                retail_price = random.randint(cost_price + 50, 40000)
                manufacture = random.choice(manufactures)
                location = random.choice(Product.PRODUCT_LOCATION_CHOICES)[1]

                # Create a Product
                Product.objects.create(
                    serial_number=serial_number,
                    name=name,
                    sku=sku,
                    qty=qty,
                    description=description,
                    cost_price=cost_price,
                    retail_price=retail_price,
                    manufacture=manufacture,
                    location=location,
                )

                self.stdout.write(self.style.SUCCESS("Products created successfully"))

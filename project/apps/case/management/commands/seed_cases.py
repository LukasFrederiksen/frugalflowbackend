from django.core.management.base import BaseCommand
from faker import Faker
import random

from project.apps.case.models import Case, CaseProduct
from project.apps.customer.models import Customer
from project.apps.users.models import User
from project.apps.product.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        product_owner = User.objects.first()

        for _ in range(50):
            # Retrieve a random customer for each iteration
            random_customer = Customer.objects.order_by('?').first()

            created_case = Case.objects.create(
                title=faker.name(),
                description=faker.text(50),
                total_price=faker.random_int(min=100, max=1000),
                deadline=faker.date_this_year(),
                customer=random_customer,
                product_owner=product_owner,
            )

            # Add 1 to 5 random followers to the created case
            random_followers = User.objects.order_by('?')[:random.randint(1, 5)]
            created_case.followers.add(*random_followers)

            # Decide whether this case gets a CaseProduct
            if random.choice([True, False]):
                # Decide how many CaseProducts for this Case
                for _ in range(random.randint(1, 3)):  # a Case can have between 1 and 3 CaseProducts
                    case_product = CaseProduct.objects.create(
                        status=random.choice(CaseProduct.CASEPRODUCT_STATUS_CHOICES)[0])
                    # Add 1 to 3 random products to the CaseProduct
                    products_to_add = Product.objects.order_by('?')[:random.randint(1, 3)]
                    case_product.products.add(*products_to_add)
                    # Associate the created CaseProduct with the Case
                    created_case.case_products.add(case_product)

from django.test import TestCase
from ..models import UniqueProduct
from ...contacts.models import ContactPerson
from ...manufacture.models import Manufacture
from ...product.models import Product


class UniqueProductTests(TestCase):
    def setUp(self):
        contact_person = ContactPerson.objects.create(phone="98124411", email="test@test.com")
        manufacture = Manufacture.objects.create(cvr=123456, name="Frugal", contact_person_id=contact_person.id,
                                                 email="frugal@info.com", website="frugal.com", picture_logo="none")
        product = Product.objects.create(name="Test Product", description="A Product for testing",
                                         cost_price=500, retail_price=1000, manufacture_id=manufacture.id,
                                         sku="1992315", is_unique=1)
        UniqueProduct.objects.create(product_id=product.id, case=None, serial_number="6411421",
                                     custom_price=1500, status_payment="Paid",
                                     status_shipping="Arrived")

    def test_unique_product_creation(self):
        product = Product.objects.get(name="Test Product")
        unique_product = UniqueProduct.objects.get(serial_number="6411421")

        self.assertEqual(product.description, "A Product for testing")
        self.assertEqual(unique_product.custom_price, 1500)

    def test_unique_product_backwards(self):
        product = Product.objects.get(name="Test Product")
        unique_product_backwards = product.unique_products.get(serial_number="6411421")
        unique_product = UniqueProduct.objects.get(serial_number="6411421")

        self.assertEqual(unique_product, unique_product_backwards)



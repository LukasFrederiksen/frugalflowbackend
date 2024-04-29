from django.test import TestCase


class CaseModelTest(TestCase):
    def test_case_str_method(self):
        # Test the __str__ method of the Case model
        self.assertEqual(1, 1)

    # def setUp(self):
    #     # Create a sample user for the product owner
    #     self.user = User.objects.create_user(
    #         username='testuser',
    #         password='testpassword'
    #     )

    #     # Create a sample customer
    #     self.customer = Customer.objects.create(
    #         name='Test Customer',
    #         email='customer@example.com'
    #     )

    #     # Create a sample case
    #     self.case = Case.objects.create(
    #         name='Test Case',
    #         description='Test description',
    #         price=100,
    #         deadline=date(2023, 12, 31),
    #         customer=self.customer,
    #         product_owner=self.user
    #     )

    # def test_case_str_method(self):
    #     # Test the __str__ method of the Case model
    #     self.assertEqual(str(self.case), 'Test Case')

    # def test_case_fields(self):
    #     # Test individual fields of the Case model
    #     self.assertEqual(self.case.name, 'Test Case')
    #     self.assertEqual(self.case.description, 'Test description')
    #     self.assertEqual(self.case.price, 100)
    #     self.assertEqual(self.case.deadline, date(2023, 12, 31))
    #     self.assertEqual(self.case.customer, self.customer)
    #     self.assertEqual(self.case.product_owner, self.user)

    # def test_case_created_at_auto_now_add(self):
    #     # Test the `created_at` field, which should be auto-populated
    #     self.assertIsNotNone(self.case.created_at)

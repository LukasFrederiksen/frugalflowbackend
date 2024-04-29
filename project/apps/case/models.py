from django.db import models

from project.apps.customer.models import Customer
from project.apps.product.models import Product
from project.apps.users.models import User
from project.apps.vessel.models import Vessel


# Model for holding the status of a product in a case
class CaseProduct(models.Model):
    products = models.ManyToManyField(Product)

    CASEPRODUCT_STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('setup', 'Setup in Progress'),
        ('closed', 'Closed'),
    )

    status = models.CharField(max_length=100, choices=CASEPRODUCT_STATUS_CHOICES, default='open')

    def __str__(self):
        # This will return a string like "ProductA, ProductB, ProductC"
        return ", ".join([product.name for product in self.products.all()])


# This is the model for the case/project
class Case(models.Model):
    class Meta:
        db_table = 'case'
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'

    # Fields
    title = models.CharField(max_length=100)
    description = models.TextField()
    total_price = models.IntegerField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Relationship Fields
    followers = models.ManyToManyField(User, related_name='following_cases')
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE, null=True, blank=True)
    product_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_cases', null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_cases')
    case_products = models.ManyToManyField(CaseProduct, related_name='cases', null=True, blank=True)

    # Choices for status fields
    CASE_STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('setup', 'Setup in Progress'),
        ('closed', 'Closed'),
        ('cancelled', 'Cancelled'),
        ('on_hold', 'On Hold'),
        ('done', 'Done'),
    )
    PAYMENT_STATUS_CHOICES = (
        ('unpaid', 'Unpaid'),
        ('partial', 'Partially Paid'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
        ('overpaid', 'Overpaid'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
        ('partially_refunded', 'Partially Refunded'),
        ('courtesy', 'Courtesy'),
    )

    # Status fields
    case_status = models.CharField(max_length=50, choices=CASE_STATUS_CHOICES, default='open')
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='unpaid')

    def __str__(self):
        return self.title

from django.db import models
from project.apps.customer.models import Customer
from project.apps.invoices.models import Invoice
from project.apps.users.models import User
from project.apps.vessel.models import Vessel


# This is the model for the case/project

class Case(models.Model):
    class Meta:
        db_table = 'case'
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'

    # Fields
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


    # Relationship Fields
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE, null=True, blank=True)
    case_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_cases', null=True, blank=True)


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
    # PAYMENT_STATUS_CHOICES = (
    #     ('unpaid', 'Unpaid'),
    #     ('partial', 'Partially Paid'),
    #     ('paid', 'Paid'),
    #     ('overdue', 'Overdue'),
    #     ('overpaid', 'Overpaid'),
    #     ('cancelled', 'Cancelled'),
    #     ('refunded', 'Refunded'),
    #     ('partially_refunded', 'Partially Refunded'),
    #     ('courtesy', 'Courtesy')
    # )
    # Status fields
    case_status = models.CharField(max_length=50, choices=CASE_STATUS_CHOICES, default='open')


    def __str__(self):
        return self.title

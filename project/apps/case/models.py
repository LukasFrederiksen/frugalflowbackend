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
    CASE_STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('setup', 'Setup in Progress'),
        ('closed', 'Closed'),
        ('cancelled', 'Cancelled'),
        ('on_hold', 'On Hold'),
        ('done', 'Done'),
    )
    case_status = models.CharField(max_length=50, choices=CASE_STATUS_CHOICES, default='open')
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_cases', null=True, blank=True)


    def __str__(self):
        return self.title

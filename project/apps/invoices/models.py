from django.db import models
from project.apps.vessel.models import Vessel


class Invoice(models.Model):
    is_completed = models.BooleanField(default=False)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE, null=True, blank=True)
    invoice_number = models.BigIntegerField()

from django.db import models

from project.apps.customer.models import Customer


class Vessel(models.Model):
    VESSEL_TYPE_CHOICES = (
        ('Container Ship', 'Container Ship'),
        ('Tanker Ship', 'Tanker Ship'),
        ('Passenger Ship', 'Passenger Ship'),
        ('War Ship', 'War Ship'),
        ('Unspecified', 'Unspecified'),
    )

    class Meta:
        db_table = 'vessel'
        verbose_name = 'Vessel'
        verbose_name_plural = 'Vessels'

    name = models.CharField(max_length=255)
    imo = models.IntegerField(null=True, blank=True)  # International Maritime Organizations identifikations-system
    type = models.CharField(max_length=100, choices=VESSEL_TYPE_CHOICES, default='Unspecified')
    isDeleted = models.BooleanField(default=False)
    vessel_owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_cases')

    def __str__(self):
        return self.name

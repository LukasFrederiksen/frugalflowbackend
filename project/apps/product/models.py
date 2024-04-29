from django.db import models
from project.apps.manufacture.models import Manufacture


class Product(models.Model):
    PRODUCT_LOCATION_CHOICES = (
        ('Frugal', 'Frugal'),
        ('Wrist', 'Wrist'),
        ('Copenhagen', 'Copenhagen'),
        ('Amsterdam', 'Amsterdam'),
    )

    serial_number = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    sku = models.CharField(max_length=50, null=True, blank=True)
    qty = models.IntegerField(default=1)
    description = models.TextField()
    cost_price = models.IntegerField()
    retail_price = models.IntegerField()
    manufacture = models.ForeignKey(Manufacture, null=True, blank=True, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    location = models.CharField(max_length=150, choices=PRODUCT_LOCATION_CHOICES, default='frugal')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']




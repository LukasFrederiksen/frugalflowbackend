from django.db import models
from project.apps.manufacture.models import Manufacture


class UniqueProduct(models.Model):
    STATUS = (
        ('Arrived', 'Arrived'),
        ('Shipping', 'Shipping'),
        ('Shipped', 'Shipped'),
        ('Not Sent', 'Not Sent'),
    )
    STATUS_PAYMENT =(
        ('Paid', 'Paid'),
        ('Awaiting Payment', 'Awaiting Payment'),
        ('Invoice Sent', 'Invoice Sent'),
        ('Invoice Not Created', 'Invoice Not Created'),
    )

    serial_number = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    sku = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    cost_price = models.IntegerField()
    retail_price = models.IntegerField()
    manufacture = models.ForeignKey(Manufacture, null=True, blank=True, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    status = models.CharField(max_length=150, choices=STATUS, default='Not Sent')
    status_payment = models.CharField(max_length=150, choices=STATUS_PAYMENT, default='Invoice Not Created')
    vessel = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'unique_product'
        verbose_name = 'Unique Product'
        verbose_name_plural = 'Unique Products'
        ordering = ['name']




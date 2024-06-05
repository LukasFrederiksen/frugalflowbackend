from django.db import models
from project.apps.case.models import Case
from project.apps.product.models import Product


class UniqueProduct(models.Model):
    STATUS_SHIPPING = (
        ('Arrived', 'Arrived'),
        ('Shipping', 'Shipping'),
        ('Shipped', 'Shipped'),
        ('Not Sent', 'Not Sent'),
    )
    STATUS_PAYMENT = (
        ('Paid', 'Paid'),
        ('Awaiting Payment', 'Awaiting Payment'),
        ('Invoice Sent', 'Invoice Sent'),
        ('Invoice Not Created', 'Invoice Not Created'),
    )

    unique_product_id = models.AutoField(primary_key=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='unique_products')

    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='unique_products', null=True, blank=True)
    serial_number = models.CharField(max_length=50, unique=True)
    custom_price = models.IntegerField(null=True, blank=True)
    status_shipping = models.CharField(max_length=150, choices=STATUS_SHIPPING, default='Shipped')
    status_payment = models.CharField(max_length=150, choices=STATUS_PAYMENT, blank=True)

    class Meta:
        db_table = 'unique_product'
        verbose_name = 'Unique_product'
        verbose_name_plural = 'Unique_products'

    def __str__(self):
        return "Unique"

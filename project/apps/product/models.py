from django.db import models

from project.apps.case.models import Case
from project.apps.manufacture.models import Manufacture


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    cost_price = models.IntegerField()
    retail_price = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, null=True, blank=True)
    sku = models.CharField(max_length=50, null=True, blank=True)
    is_unique = models.BooleanField(default=0)
    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name


class SimpleProduct(Product):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='simple_products', null=True, blank=True)
    qty = models.IntegerField()


    class Meta:
        db_table = 'simple_product'
        verbose_name = 'Simple_product'
        verbose_name_plural = 'Simple_products'

    def __str__(self):
        return "Simple Product"


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

from django.db import models

from project.apps import case


class Customer(models.Model):
    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    cases = models.ManyToManyField('case.Case', related_name='customers', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    customer_picture = models.URLField()

    def __str__(self):
        return self.name

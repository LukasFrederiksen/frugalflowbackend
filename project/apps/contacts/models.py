from django.db import models


class ContactPerson(models.Model):
    class Meta:
        db_table = 'contact_person'
        verbose_name = 'Contact Person'
        verbose_name_plural = 'Contact Persons'

    phone = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=100)

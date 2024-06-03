from django.db import models


class ContactPerson(models.Model):
    phone = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=100)

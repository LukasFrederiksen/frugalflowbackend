from django import forms
from django.db import models
from project.apps.contacts.models import ContactPerson


class Manufacture(models.Model):
    class Meta:
        db_table = 'manufacture'
        verbose_name = 'Manufacture'
        verbose_name_plural = 'Manufactures'

    cvr = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=70, unique=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    picture_logo = models.URLField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UploadImage(forms.ModelForm):
    class Meta:
        model = Manufacture
        fields = ['picture_logo']

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Meta:
        db_table = 'user'

    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    #   Original fields from AbstractUser, made required
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)



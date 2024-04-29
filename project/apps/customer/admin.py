from django.contrib import admin

# Register your models here.
from project.apps.customer.models import Customer

admin.site.register(Customer)

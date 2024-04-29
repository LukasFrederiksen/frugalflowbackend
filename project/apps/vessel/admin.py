from django.contrib import admin

# Register your models here.
from project.apps.vessel.models import Vessel

admin.site.register(Vessel)

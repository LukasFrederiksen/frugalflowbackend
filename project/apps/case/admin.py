from django.contrib import admin

# Register your models here.
from project.apps.case.models import Case

admin.site.register(Case)

# Generated by Django 5.0.6 on 2024-06-05 11:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('case', '0001_initial'),
        ('vessel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='case_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_cases', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='case',
            name='vessel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vessel.vessel'),
        ),
    ]

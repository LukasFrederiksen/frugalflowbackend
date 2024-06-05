# Generated by Django 5.0.6 on 2024-06-05 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('imo', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Container Ship', 'Container Ship'), ('Tanker Ship', 'Tanker Ship'), ('Passenger Ship', 'Passenger Ship'), ('War Ship', 'War Ship'), ('Unspecified', 'Unspecified')], default='Unspecified', max_length=100)),
                ('isDeleted', models.BooleanField(default=False)),
                ('vessel_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_cases', to='customer.customer')),
            ],
            options={
                'verbose_name': 'Vessel',
                'verbose_name_plural': 'Vessels',
                'db_table': 'vessel',
            },
        ),
    ]

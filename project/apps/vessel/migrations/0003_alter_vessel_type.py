# Generated by Django 4.2.5 on 2023-11-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vessel', '0002_vessel_imo_vessel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vessel',
            name='type',
            field=models.CharField(choices=[('container ship', 'Container Ship'), ('tanker ship', 'Tanker Ship'), ('passenger ship', 'Passenger Ship'), ('war ship', 'War Ship')], default='cargo ship', max_length=100),
        ),
    ]

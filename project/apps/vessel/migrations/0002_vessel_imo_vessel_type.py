# Generated by Django 4.2.5 on 2023-10-21 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vessel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vessel',
            name='imo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vessel',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

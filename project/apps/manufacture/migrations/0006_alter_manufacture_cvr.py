# Generated by Django 4.2.5 on 2023-10-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacture', '0005_alter_manufacture_cvr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacture',
            name='cvr',
            field=models.IntegerField(blank=True),
        ),
    ]

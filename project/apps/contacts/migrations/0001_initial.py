# Generated by Django 5.0.6 on 2024-06-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Contact Person',
                'verbose_name_plural': 'Contact Persons',
                'db_table': 'contact_person',
            },
        ),
    ]

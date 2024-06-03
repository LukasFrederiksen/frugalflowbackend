# Generated by Django 4.2.5 on 2024-05-31 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vessel', '0004_alter_vessel_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('invoice_number', models.BigIntegerField()),
                ('vessel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vessel.vessel')),
            ],
        ),
    ]
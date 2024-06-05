# Generated by Django 5.0.6 on 2024-06-05 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('case', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueProduct',
            fields=[
                ('unique_product_id', models.AutoField(primary_key=True, serialize=False)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('custom_price', models.IntegerField(blank=True, null=True)),
                ('status_shipping', models.CharField(choices=[('Arrived', 'Arrived'), ('Shipping', 'Shipping'), ('Shipped', 'Shipped'), ('Not Sent', 'Not Sent')], default='Shipped', max_length=150)),
                ('status_payment', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Awaiting Payment', 'Awaiting Payment'), ('Invoice Sent', 'Invoice Sent'), ('Invoice Not Created', 'Invoice Not Created')], max_length=150)),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unique_products', to='case.case')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unique_products', to='product.product')),
            ],
            options={
                'verbose_name': 'Unique_product',
                'verbose_name_plural': 'Unique_products',
                'db_table': 'unique_product',
            },
        ),
    ]
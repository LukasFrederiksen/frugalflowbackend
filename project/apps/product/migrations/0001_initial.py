# Generated by Django 5.0.6 on 2024-06-05 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('case', '0001_initial'),
        ('manufacture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cost_price', models.IntegerField()),
                ('retail_price', models.IntegerField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('sku', models.CharField(blank=True, max_length=50, null=True)),
                ('is_unique', models.BooleanField(default=0)),
                ('manufacture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacture.manufacture')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SimpleProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('qty', models.IntegerField()),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='simple_products', to='case.case')),
            ],
            options={
                'verbose_name': 'Simple_product',
                'verbose_name_plural': 'Simple_products',
                'db_table': 'simple_product',
            },
            bases=('product.product',),
        ),
    ]
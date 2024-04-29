# Generated by Django 4.2.5 on 2023-10-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_isdeleted_product_is_deleted'),
        ('case', '0004_rename_name_case_title_rename_price_case_total_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caseproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='caseproduct',
            name='products',
            field=models.ManyToManyField(to='product.product'),
        ),
    ]

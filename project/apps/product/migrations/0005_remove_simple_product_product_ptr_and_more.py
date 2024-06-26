# Generated by Django 4.2.5 on 2023-11-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_composite_product_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simple_product',
            name='product_ptr',
        ),
        migrations.RemoveField(
            model_name='unique_product',
            name='product_ptr',
        ),
        migrations.AddField(
            model_name='product',
            name='serial_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Composite_product',
        ),
        migrations.DeleteModel(
            name='Simple_product',
        ),
        migrations.DeleteModel(
            name='Unique_product',
        ),
    ]

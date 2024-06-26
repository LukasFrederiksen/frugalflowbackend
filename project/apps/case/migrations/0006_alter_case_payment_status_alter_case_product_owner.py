# Generated by Django 4.2.5 on 2023-11-06 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('case', '0005_remove_caseproduct_product_caseproduct_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='payment_status',
            field=models.CharField(choices=[('unpaid', 'Unpaid'), ('partial', 'Partially Paid'), ('paid', 'Paid'), ('overdue', 'Overdue'), ('overpaid', 'Overpaid'), ('cancelled', 'Cancelled'), ('refunded', 'Refunded'), ('partially_refunded', 'Partially Refunded'), ('courtesy', 'Courtesy')], default='unpaid', max_length=50),
        ),
        migrations.AlterField(
            model_name='case',
            name='product_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_cases', to=settings.AUTH_USER_MODEL),
        ),
    ]

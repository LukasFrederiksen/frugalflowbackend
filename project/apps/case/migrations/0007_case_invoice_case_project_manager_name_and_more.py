# Generated by Django 4.2.5 on 2024-05-31 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
        ('case', '0006_alter_case_payment_status_alter_case_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice'),
        ),
        migrations.AddField(
            model_name='case',
            name='project_manager_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_products',
            field=models.ManyToManyField(blank=True, null=True, related_name='cases', to='case.caseproduct'),
        ),
    ]

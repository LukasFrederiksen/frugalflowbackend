# Generated by Django 5.0.6 on 2024-06-05 20:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vessel', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('deadline', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('case_status', models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('setup', 'Setup in Progress'), ('closed', 'Closed'), ('cancelled', 'Cancelled'), ('on_hold', 'On Hold'), ('done', 'Done')], default='open', max_length=50)),
                ('case_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_cases', to=settings.AUTH_USER_MODEL)),
                ('vessel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vessel.vessel')),
            ],
            options={
                'verbose_name': 'Case',
                'verbose_name_plural': 'Cases',
                'db_table': 'case',
            },
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvr', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('contactperson', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('website', models.CharField(max_length=255)),
                ('picture_logo', models.ImageField(upload_to='images/')),
                ('isdeleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Manufacture',
                'verbose_name_plural': 'Manufactures',
                'db_table': 'manufacture',
            },
        ),
    ]

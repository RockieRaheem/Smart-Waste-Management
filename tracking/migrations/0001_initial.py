# Generated by Django 4.2.9 on 2025-03-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GarbageTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=100)),
                ('license_plate', models.CharField(max_length=20, unique=True)),
                ('current_location', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

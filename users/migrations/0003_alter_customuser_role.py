# Generated by Django 5.1.7 on 2025-03-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('resident', 'Resident'), ('driver', 'Truck Driver'), ('company', 'Waste Management Company'), ('officer', 'Municipal Officer')], default='resident', max_length=20),
        ),
    ]

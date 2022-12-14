# Generated by Django 4.1.3 on 2022-11-28 22:13

import django.core.validators
from django.db import migrations, models
import system_for_remote_meter_points.meter_devices.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeterDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_device_number', models.CharField(max_length=16, unique=True, validators=[django.core.validators.MinLengthValidator(16), system_for_remote_meter_points.meter_devices.models.only_int])),
                ('meter_device_type', models.TextField(choices=[('ISKRA', 'ISKRA'), ('GAMA', 'GAMA'), ('AMT', 'AMT'), ('Microstar', 'Microstar')])),
            ],
        ),
    ]

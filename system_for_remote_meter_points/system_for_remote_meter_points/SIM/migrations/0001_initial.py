# Generated by Django 4.1.3 on 2022-11-28 22:13

import django.core.validators
from django.db import migrations, models
import system_for_remote_meter_points.SIM.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SIM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sim_number', models.CharField(max_length=16, unique=True, validators=[django.core.validators.MinLengthValidator(14), system_for_remote_meter_points.SIM.models.only_int])),
                ('gsm_number', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10), system_for_remote_meter_points.SIM.models.only_int])),
                ('ip_address', models.GenericIPAddressField()),
                ('operator', models.TextField(choices=[('А1', 'А1'), ('Yettel', 'Yettel'), ('Vivacom', 'Vivacom')])),
            ],
        ),
    ]

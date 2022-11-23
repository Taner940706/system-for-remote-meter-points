# Generated by Django 4.1.3 on 2022-11-23 20:18

from django.db import migrations, models
import django.db.models.deletion
import system_for_remote_meter_points.meter_devices.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meter_points', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeterDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_device_number', models.TextField(unique=True, validators=[system_for_remote_meter_points.meter_devices.models.validate_length, system_for_remote_meter_points.meter_devices.models.only_int])),
                ('meter_device_type', models.TextField(choices=[('ISKRA', 'ISKRA'), ('GAMA', 'GAMA'), ('AMT', 'AMT'), ('Microstar', 'Microstar')])),
                ('meter_point', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meter_points.meterpoint')),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter_devices', '0007_alter_meterdevice_meter_device_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterdevice',
            name='meter_device_read_cycle',
            field=models.TextField(choices=[('', 'Read cycle'), ('Read per 15 minute', 'Read per 15 minute'), ('Read per 1 hour', 'Read per 1 hour'), ('Read per 8 hours', 'Read per 8 hours'), ('Read per 24 hours', 'Read per 24 hours')]),
        ),
        migrations.AlterField(
            model_name='meterdevice',
            name='meter_device_type',
            field=models.TextField(choices=[('', 'Meter device type'), ('ISKRA', 'ISKRA'), ('GAMA', 'GAMA'), ('AMT', 'AMT'), ('Microstar', 'Microstar')]),
        ),
    ]

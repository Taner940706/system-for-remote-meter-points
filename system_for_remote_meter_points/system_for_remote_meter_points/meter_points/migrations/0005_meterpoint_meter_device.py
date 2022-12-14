# Generated by Django 4.1.3 on 2022-11-24 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meter_devices', '0006_meterdevice_meter_point'),
        ('meter_points', '0004_meterpoint_modem'),
    ]

    operations = [
        migrations.AddField(
            model_name='meterpoint',
            name='meter_device',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='meter_device_meter_point_key', to='meter_devices.meterdevice'),
            preserve_default=False,
        ),
    ]

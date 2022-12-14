# Generated by Django 4.1.3 on 2022-12-09 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meter_devices', '0005_alter_meterdevice_user'),
        ('modems', '0005_alter_modem_sim'),
        ('meter_points', '0008_alter_meterpoint_meter_device_alter_meterpoint_modem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterpoint',
            name='meter_device',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='meter_device_meter_point_key', to='meter_devices.meterdevice', to_field='meter_device_number'),
        ),
        migrations.AlterField(
            model_name='meterpoint',
            name='modem',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='modem_meter_point_key', to='modems.modem', to_field='modem_number'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter_devices', '0009_alter_meterdevice_meter_device_read_cycle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterdevice',
            name='meter_device_type',
            field=models.TextField(choices=[('DoNotShow', 'Meter device type:'), ('ISKRA', 'ISKRA'), ('GAMA', 'GAMA'), ('AMT', 'AMT'), ('MICROSTAR', 'Microstar')]),
        ),
    ]
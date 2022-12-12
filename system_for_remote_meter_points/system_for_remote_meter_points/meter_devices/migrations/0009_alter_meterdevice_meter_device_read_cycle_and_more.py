# Generated by Django 4.1.3 on 2022-12-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter_devices', '0008_alter_meterdevice_meter_device_read_cycle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterdevice',
            name='meter_device_read_cycle',
            field=models.TextField(choices=[('READ_PER_15_MIN', 'Read per 15 minute'), ('READ_PER_1_HOUR', 'Read per 1 hour'), ('READ_PER_8_HOURS', 'Read per 8 hours'), ('READ_PER_24_HOURS', 'Read per 24 hours')]),
        ),
        migrations.AlterField(
            model_name='meterdevice',
            name='meter_device_type',
            field=models.TextField(choices=[('ISKRA', 'ISKRA'), ('GAMA', 'GAMA'), ('AMT', 'AMT'), ('MICROSTAR', 'Microstar')]),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter_devices', '0012_alter_meterdevice_meter_device_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterdevice',
            name='meter_device_type',
            field=models.TextField(choices=[('ISKRA', 'ISKRA'), ('GAMA', 'GAMA'), ('AMT', 'AMT'), ('MICROSTAR', 'Microstar')]),
        ),
    ]

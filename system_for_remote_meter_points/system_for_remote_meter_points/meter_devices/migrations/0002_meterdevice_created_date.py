# Generated by Django 4.1.3 on 2022-11-29 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter_devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meterdevice',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]
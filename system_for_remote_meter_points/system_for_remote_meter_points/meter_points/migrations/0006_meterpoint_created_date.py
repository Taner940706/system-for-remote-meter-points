# Generated by Django 4.1.3 on 2022-11-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter_points', '0005_meterpoint_meter_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='meterpoint',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]
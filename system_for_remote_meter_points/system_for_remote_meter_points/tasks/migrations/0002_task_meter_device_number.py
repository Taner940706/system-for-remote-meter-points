# Generated by Django 4.1.3 on 2022-11-25 09:39

from django.db import migrations, models
import system_for_remote_meter_points.tasks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='meter_device_number',
            field=models.TextField(default=1, unique=True, validators=[system_for_remote_meter_points.tasks.models.validate_length, system_for_remote_meter_points.tasks.models.only_int]),
            preserve_default=False,
        ),
    ]

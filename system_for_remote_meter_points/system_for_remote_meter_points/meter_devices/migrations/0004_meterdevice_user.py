# Generated by Django 4.1.3 on 2022-11-29 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meter_devices', '0003_meterdevice_meter_device_read_cycle'),
    ]

    operations = [
        migrations.AddField(
            model_name='meterdevice',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, to_field='username'),
            preserve_default=False,
        ),
    ]
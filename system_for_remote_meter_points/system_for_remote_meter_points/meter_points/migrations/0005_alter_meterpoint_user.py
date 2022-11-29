# Generated by Django 4.1.3 on 2022-11-29 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meter_points', '0004_alter_meterpoint_operation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterpoint',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, to_field='username'),
            preserve_default=False,
        ),
    ]

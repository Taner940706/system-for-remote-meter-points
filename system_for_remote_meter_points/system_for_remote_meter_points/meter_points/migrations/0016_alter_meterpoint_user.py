# Generated by Django 4.1.3 on 2022-12-13 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meter_points', '0015_alter_meterpoint_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterpoint',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
# Generated by Django 4.1.3 on 2022-11-24 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meter_points', '0002_remove_meterpoint_ip_address_meterpoint_comment_and_more'),
        ('modems', '0002_alter_modem_meter_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modem',
            name='meter_point',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meter_points.meterpoint'),
        ),
    ]
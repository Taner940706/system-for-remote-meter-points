# Generated by Django 4.1.3 on 2022-11-24 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modems', '0003_alter_modem_meter_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modem',
            name='meter_point',
        ),
    ]
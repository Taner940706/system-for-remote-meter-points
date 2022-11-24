# Generated by Django 4.1.3 on 2022-11-24 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modems', '0004_remove_modem_meter_point'),
        ('SIM', '0004_sim_modem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sim',
            name='modem',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modem_key', to='modems.modem'),
        ),
    ]
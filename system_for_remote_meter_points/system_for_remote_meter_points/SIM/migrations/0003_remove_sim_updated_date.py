# Generated by Django 4.1.3 on 2022-11-28 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SIM', '0002_sim_updated_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sim',
            name='updated_date',
        ),
    ]

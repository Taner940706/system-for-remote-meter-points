# Generated by Django 4.1.3 on 2022-12-13 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meter_points', '0012_alter_meterpoint_operation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterpoint',
            name='operation',
            field=models.TextField(choices=[('Restore communication', 'RESTORE_COMM'), ('Add new meter points', 'ADD_NEW_METER_POINT'), ('Replace meter device', 'REPLACE_MEW_METER_DEVICE'), ('Replace modem and/or SIM card', 'REPLACE_NEW_MODEM_OR_SIM'), ('Delete meter points', 'DELETE_METER_POINT'), ('Add new constant', 'REPLACE_NEW_CONSTANT'), ('Other (in ,,Comment")', 'OTHER')]),
        ),
        migrations.AlterField(
            model_name='meterpoint',
            name='regional_center',
            field=models.TextField(choices=[('Varna', 'VARNA'), ('Dobrich', 'DOBRICH'), ('Shumen', 'SHUMEN'), ('Targovishte', 'TARGOVISHTE'), ('Veliko Tarnovo', 'TARNOVO'), ('Ruse', 'RUSE'), ('Razgrad', 'RAZGRAD'), ('Silistra', 'SILISTRA'), ('Gabrovo', 'GABROVO')]),
        ),
        migrations.AlterField(
            model_name='meterpoint',
            name='result_operation',
            field=models.TextField(choices=[('No communication', 'NO_COMM'), ('Successful communication', 'YES_COMM'), ('In progress...', 'WAIT_COMM')]),
        ),
        migrations.AlterField(
            model_name='meterpoint',
            name='user',
            field=models.ForeignKey(default='username', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AlterField(
            model_name='meterpoint',
            name='voltage',
            field=models.TextField(choices=[('Low', 'LOW'), ('Medium', 'MEDIUM'), ('High', 'HIGH')]),
        ),
    ]

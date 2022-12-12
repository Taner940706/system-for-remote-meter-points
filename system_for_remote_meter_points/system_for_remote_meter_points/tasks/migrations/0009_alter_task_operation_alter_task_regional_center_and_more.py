# Generated by Django 4.1.3 on 2022-12-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_alter_task_operation_alter_task_regional_center_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='operation',
            field=models.TextField(choices=[('RESTORE_COMM', 'Restore communication'), ('ADD_NEW_METER_POINT', 'Add new meter points'), ('REPLACE_MEW_METER_DEVICE', 'Replace meter device'), ('REPLACE_NEW_MODEM_OR_SIM', 'Replace modem and/or SIM card'), ('DELETE_METER_POINT', 'Delete meter points'), ('REPLACE_NEW_CONSTANT', 'Add new constant'), ('OTHER', 'Other (in ,,Comment")')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='regional_center',
            field=models.TextField(choices=[('VARNA', 'Varna'), ('DOBRICH', 'Dobrich'), ('SHUMEN', 'Shumen'), ('TARGOVISHTE', 'Targovishte'), ('TARNOVO', 'Veliko Tarnovo'), ('RUSE', 'Ruse'), ('RAZGRAD', 'Razgrad'), ('SILISTRA', 'Silistra'), ('GABROVO', 'Gabrovo')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='result_operation',
            field=models.TextField(choices=[('NO_COMM', 'No communication'), ('YES_COMM', 'Successful communication'), ('WAIT_COMM', 'In progress...')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='voltage',
            field=models.TextField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')]),
        ),
    ]

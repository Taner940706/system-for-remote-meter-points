# Generated by Django 4.1.3 on 2022-11-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter_points', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meterpoint',
            name='ip_address',
        ),
        migrations.AddField(
            model_name='meterpoint',
            name='comment',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='meterpoint',
            name='operation',
            field=models.TextField(choices=[('Възсатновяване на комуникация', 'Възсатновяване на комуникация'), ('Добавяне на нова точка', 'Добавяне на нова точка'), ('Подмяна на електромер', 'Подмяна на електромер'), ('Подмяна на модем и/или СИМ карта', 'Подмяна на модем и/или СИМ карта'), ('Изтриване на точка', 'Изтриване на точка'), ('Смяна на константа', 'Смяна на константа'), ('Друго (в ,,Коментарите"")', 'Друго (в ,,Коментарите"")')], default=''),
        ),
        migrations.AddField(
            model_name='meterpoint',
            name='result_operation',
            field=models.TextField(choices=[('Няма комуникация', 'Няма комуникация'), ('Има комуникация', 'Има комуникация'), ('В процес на изпълнение...', 'В процес на изпълнение...')], default=''),
        ),
    ]

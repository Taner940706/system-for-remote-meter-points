# Generated by Django 4.1.3 on 2022-11-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='username',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

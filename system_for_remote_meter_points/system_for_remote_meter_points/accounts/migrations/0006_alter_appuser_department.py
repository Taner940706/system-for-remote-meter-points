# Generated by Django 4.1.3 on 2022-12-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_appuser_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='department',
            field=models.TextField(choices=[('DOSO', 'DOSO'), ('OSP', 'OSP'), ('Auditor', 'AUDITOR'), ('Other', 'OTHER')]),
        ),
    ]

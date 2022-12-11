# Generated by Django 4.1.3 on 2022-12-11 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SIM', '0004_alter_sim_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sim',
            name='user',
            field=models.ForeignKey(default='Unknown', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.


def validate_length(value, FIXED_MODEM_NUMBER_LENGTH):
    if len(str(value)) != FIXED_MODEM_NUMBER_LENGTH:
        raise ValidationError(u'%s is not the correct length' % value)


def only_int(value):
    if not value.isdigit():
        raise ValidationError('Contains characters')


class Modem(models.Model):

    FIXED_MODEM_NUMBER_LENGTH = 6

    modem_number = models.TextField(
        validators=(
            validate_length, only_int),
        unique=True,
        blank=False,
        null=False,)
    sim = models.OneToOneField(
        'SIM.SIM',
        related_name='sim_key',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )
    meter_point = models.OneToOneField(
        'meter_points.MeterPoint',
        related_name='meter_point_modem_key',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )




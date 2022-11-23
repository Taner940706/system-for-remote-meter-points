from django.core.exceptions import ValidationError
from django.db import models

from system_for_remote_meter_points.meter_points.models import MeterPoint


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
    meter_point = models.OneToOneField(
        MeterPoint,
        on_delete=models.PROTECT,
    )



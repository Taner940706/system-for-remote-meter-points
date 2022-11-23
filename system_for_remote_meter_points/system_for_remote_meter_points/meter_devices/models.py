from django.core.exceptions import ValidationError

# Create your models here.
from django.db import models

from system_for_remote_meter_points.meter_points.models import MeterPoint


# Create your models here.


def validate_length(value, FIXED_METER_DEVICE_NUMBER_LENGTH):
    if len(str(value))!=FIXED_METER_DEVICE_NUMBER_LENGTH:
        raise ValidationError(u'%s is not the correct length' % value)


def only_int(value):
    if not value.isdigit():
        raise ValidationError('Contains characters')


class MeterDevice(models.Model):

    FIXED_METER_DEVICE_NUMBER_LENGTH = 16

    ISKRA = 'ISKRA'
    GAMA = 'GAMA'
    AMT = 'AMT'
    MICROSTAR = 'Microstar'

    METER_DEVICE_TYPE = (
        (ISKRA, ISKRA),
        (GAMA, GAMA),
        (AMT, AMT),
        (MICROSTAR, MICROSTAR),
    )

    meter_device_number = models.TextField(
        validators=(validate_length,
                    only_int,),
        unique=True,
        blank=False,
        null=False,)
    meter_device_type = models.TextField(
        choices=METER_DEVICE_TYPE,
        null=False,
        blank=False,
    )
    
    meter_point = models.ForeignKey(
        MeterPoint,
        on_delete=models.PROTECT,
    )

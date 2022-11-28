from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

# Create your models here.
from django.db import models



# Create your models here.

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

    meter_device_number = models.CharField(
        max_length=FIXED_METER_DEVICE_NUMBER_LENGTH,
        validators=(MinLengthValidator(FIXED_METER_DEVICE_NUMBER_LENGTH),
                    only_int,),
        unique=True,
        blank=False,
        null=False,)
    meter_device_type = models.TextField(
        choices=METER_DEVICE_TYPE,
        null=False,
        blank=False,
    )
    meter_point = models.OneToOneField(
        'meter_points.MeterPoint',
        related_name='meter_point_meter_device_key',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

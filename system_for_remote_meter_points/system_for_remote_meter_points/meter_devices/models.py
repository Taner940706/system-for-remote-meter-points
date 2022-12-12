from enum import Enum

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator

from django.db import models

from system_for_remote_meter_points.core.model_mixins import ChoicesEnumMixin
from system_for_remote_meter_points.core.validators import only_int

UserModel = get_user_model()


class MeterDeviceType(ChoicesEnumMixin, Enum):
    ISKRA = 'ISKRA'
    GAMA = 'GAMA'
    AMT = 'AMT'
    MICROSTAR = 'Microstar'


class ReadCycle(ChoicesEnumMixin, Enum):
    READ_PER_15_MIN = 'Read per 15 minute'
    READ_PER_1_HOUR = 'Read per 1 hour'
    READ_PER_8_HOURS = 'Read per 8 hours'
    READ_PER_24_HOURS = 'Read per 24 hours'


class MeterDevice(models.Model):
    FIXED_METER_DEVICE_NUMBER_LENGTH = 16

    # ISKRA = 'ISKRA'
    # GAMA = 'GAMA'
    # AMT = 'AMT'
    # MICROSTAR = 'Microstar'

    READ_PER_15_MIN = 'Read per 15 minute'
    READ_PER_1_HOUR = 'Read per 1 hour'
    READ_PER_8_HOURS = 'Read per 8 hours'
    READ_PER_24_HOURS = 'Read per 24 hours'

    # METER_DEVICE_TYPE = (
    #     ('', 'Meter device type'),
    #     (ISKRA, ISKRA),
    #     (GAMA, GAMA),
    #     (AMT, AMT),
    #     (MICROSTAR, MICROSTAR),
    # )

    # READ_CYCLE = (
    #     ('', 'Read cycle'),
    #     (READ_PER_15_MIN, READ_PER_15_MIN),
    #     (READ_PER_1_HOUR, READ_PER_1_HOUR),
    #     (READ_PER_8_HOURS, READ_PER_8_HOURS),
    #     (READ_PER_24_HOURS, READ_PER_24_HOURS),
    # )

    meter_device_number = models.CharField(
        max_length=FIXED_METER_DEVICE_NUMBER_LENGTH,
        validators=(MinLengthValidator(FIXED_METER_DEVICE_NUMBER_LENGTH),
                    only_int,),
        unique=True,
        blank=False,
        null=False, )
    meter_device_type = models.TextField(
        choices=MeterDeviceType.choices(),
        null=False,
        blank=False,
    )
    meter_device_read_cycle = models.TextField(
        choices=ReadCycle.choices(),
        null=False,
        blank=False,
    )
    created_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        to_field='username',
        default="Unknown",
        on_delete=models.SET_DEFAULT,
        null=True,
    )

    def __str__(self):
        return self.meter_device_number

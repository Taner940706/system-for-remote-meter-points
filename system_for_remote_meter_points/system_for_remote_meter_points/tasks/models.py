from enum import Enum

from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models
from system_for_remote_meter_points.core.model_mixins import ChoicesEnumMixin
from system_for_remote_meter_points.core.validators import only_int


# operation choice
class Operation(ChoicesEnumMixin, Enum):
    RESTORE_COMM = 'Restore communication'
    ADD_NEW_METER_POINT = 'Add new meter points'
    REPLACE_MEW_METER_DEVICE = 'Replace meter device'
    REPLACE_NEW_MODEM_OR_SIM = 'Replace modem and/or SIM card'
    DELETE_METER_POINT = 'Delete meter points'
    REPLACE_NEW_CONSTANT = 'Add new constant'
    OTHER = 'Other (in ,,Comment")'


# result operation choice
class ResultOperation(ChoicesEnumMixin, Enum):
    NO_COMM = 'No communication'
    YES_COMM = 'Successful communication'
    WAIT_COMM = 'In progress...'


# voltage choice
class Voltage(ChoicesEnumMixin, Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'


# regional center choice
class RegionalCenter(ChoicesEnumMixin, Enum):
    VARNA = 'Varna'
    DOBRICH = 'Dobrich'
    SHUMEN = 'Shumen'
    TARGOVISHTE = 'Targovishte'
    TARNOVO = 'Veliko Tarnovo'
    RUSE = 'Ruse'
    RAZGRAD = 'Razgrad'
    SILISTRA = 'Silistra'
    GABROVO = 'Gabrovo'


class Task(models.Model):
    MAX_MP_LENGTH = 50
    MIN_MP_LENGTH = 5
    MAX_CONSTANT_VALUE = 80000
    MIN_CONSTANT_VALUE = 1
    FIXED_METER_DEVICE_NUMBER_LENGTH = 16
    FIXED_MODEM_NUMBER_LENGTH = 6

    mp_name = models.CharField(
        max_length=MAX_MP_LENGTH,
        validators=(
            MinLengthValidator(MIN_MP_LENGTH),),
        blank=False,
        null=False, )
    constant = models.PositiveIntegerField(
        validators=(MaxValueValidator(MAX_CONSTANT_VALUE), MinValueValidator(MIN_CONSTANT_VALUE)),
        blank=False,
        null=False, )
    voltage = models.TextField(
        choices=Voltage.choices(),
        null=False,
        blank=False,
    )
    regional_center = models.TextField(
        choices=RegionalCenter.choices(),
        null=False,
        blank=False,
    )
    operation = models.TextField(
        choices=Operation.choices(),
        null=False,
        blank=False,
    )
    result_operation = models.TextField(
        choices=ResultOperation.choices(),
        null=False,
        blank=False,
    )
    comment = models.TextField(
        blank=True,
        null=True,
    )

    modem = models.CharField(
        max_length=FIXED_MODEM_NUMBER_LENGTH,
        validators=(only_int, MinLengthValidator(FIXED_MODEM_NUMBER_LENGTH),),
        blank=False,
        null=False, )

    meter_device = models.CharField(
        max_length=FIXED_METER_DEVICE_NUMBER_LENGTH,
        validators=(MinLengthValidator(FIXED_METER_DEVICE_NUMBER_LENGTH),
                    only_int,),
        blank=False,
        null=False, )

    created_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )
    username = models.TextField(
        blank=False,
        null=False,
    )

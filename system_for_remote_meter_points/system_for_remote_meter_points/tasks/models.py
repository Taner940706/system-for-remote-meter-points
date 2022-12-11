from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models


def only_int(value):
    if not value.isdigit():
        raise ValidationError('Contains characters')


class Task(models.Model):
    MAX_MP_LENGTH = 50
    MIN_MP_LENGTH = 5
    MAX_CONSTANT_VALUE = 80000
    MIN_CONSTANT_VALUE = 1
    FIXED_METER_DEVICE_NUMBER_LENGTH = 16
    FIXED_MODEM_NUMBER_LENGTH = 6

    RESTORE_COMM = 'Restore communication'
    ADD_NEW_METER_POINT = 'Add new meter points'
    REPLACE_MEW_METER_DEVICE = 'Replace meter device'
    REPLACE_NEW_MODEM_OR_SIM = 'Replace modem and/or SIM card'
    DELETE_METER_POINT = 'Delete meter points'
    REPLACE_NEW_CONSTANT = 'Add new constant'
    OTHER = 'Other (in ,,Comment")'

    NO_COMM = 'No communication'
    YES_COMM = 'Successful communication'
    WAIT_COMM = 'In progress...'

    OPERATION = (
        ('', 'Operation'),
        (RESTORE_COMM, RESTORE_COMM),
        (ADD_NEW_METER_POINT, ADD_NEW_METER_POINT),
        (REPLACE_MEW_METER_DEVICE, REPLACE_MEW_METER_DEVICE),
        (REPLACE_NEW_MODEM_OR_SIM, REPLACE_NEW_MODEM_OR_SIM),
        (DELETE_METER_POINT, DELETE_METER_POINT),
        (REPLACE_NEW_CONSTANT, REPLACE_NEW_CONSTANT),
        (OTHER, OTHER),
    )

    RESULT_OPERATION = (
        ('', 'Result'),
        (NO_COMM, NO_COMM),
        (YES_COMM, YES_COMM),
        (WAIT_COMM, WAIT_COMM),
    )

    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

    VARNA = 'Varna'
    DOBRICH = 'Dobrich'
    SHUMEN = 'Shumen'
    TARGOVISHTE = 'Targovishte'
    TARNOVO = 'Veliko Tarnovo'
    RUSE = 'Ruse'
    RAZGRAD = 'Razgrad'
    SILISTRA = 'Silistra'
    GABROVO = 'Gabrovo'

    VOLTAGE = (
        ('', 'Voltage'),
        (LOW, LOW),
        (MEDIUM, MEDIUM),
        (HIGH, HIGH),
    )

    REGIONAL_CENTER = (
        ('', 'Regional center'),
        (VARNA, VARNA),
        (DOBRICH, DOBRICH),
        (SHUMEN, SHUMEN),
        (TARGOVISHTE, TARGOVISHTE),
        (TARNOVO, TARNOVO),
        (RUSE, RUSE),
        (RAZGRAD, RAZGRAD),
        (SILISTRA, SILISTRA),
        (GABROVO, GABROVO),
    )

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
        choices=VOLTAGE,
        null=False,
        blank=False,
    )
    regional_center = models.TextField(
        choices=REGIONAL_CENTER,
        null=False,
        blank=False,
    )
    operation = models.TextField(
        choices=OPERATION,
        null=False,
        blank=False,
    )
    result_operation = models.TextField(
        choices=RESULT_OPERATION,
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
        # Automatically sets current date on `save` (update or create)
        auto_now=True,
        null=False,
        blank=True,
    )
    username = models.TextField(
        blank=False,
        null=False,
    )

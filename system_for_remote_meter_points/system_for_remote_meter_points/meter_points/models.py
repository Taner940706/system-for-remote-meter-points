from enum import Enum

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models

from system_for_remote_meter_points.core.model_mixins import ChoicesEnumMixin

UserModel = get_user_model()


class Operation(ChoicesEnumMixin, Enum):
    RESTORE_COMM = 'Restore communication'
    ADD_NEW_METER_POINT = 'Add new meter points'
    REPLACE_MEW_METER_DEVICE = 'Replace meter device'
    REPLACE_NEW_MODEM_OR_SIM = 'Replace modem and/or SIM card'
    DELETE_METER_POINT = 'Delete meter points'
    REPLACE_NEW_CONSTANT = 'Add new constant'
    OTHER = 'Other (in ,,Comment")'


class ResultOperation(ChoicesEnumMixin, Enum):
    NO_COMM = 'No communication'
    YES_COMM = 'Successful communication'
    WAIT_COMM = 'In progress...'


class Voltage(ChoicesEnumMixin, Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'


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


class MeterPoint(models.Model):
    MAX_MP_LENGTH = 50
    MIN_MP_LENGTH = 5
    MAX_CONSTANT_VALUE = 80000
    MIN_CONSTANT_VALUE = 1
    FIXED_METER_DEVICE_NUMBER_LENGTH = 16

    # RESTORE_COMM = 'Restore communication'
    # ADD_NEW_METER_POINT = 'Add new meter points'
    # REPLACE_MEW_METER_DEVICE = 'Replace meter device'
    # REPLACE_NEW_MODEM_OR_SIM = 'Replace modem and/or SIM card'
    # DELETE_METER_POINT = 'Delete meter points'
    # REPLACE_NEW_CONSTANT = 'Add new constant'
    # OTHER = 'Other (in ,,Comment")'

    # NO_COMM = 'No communication'
    # YES_COMM = 'Successful communication'
    # WAIT_COMM = 'In progress...'

    # OPERATION = (
    #     ('', 'Operation'),
    #     (RESTORE_COMM, RESTORE_COMM),
    #     (ADD_NEW_METER_POINT, ADD_NEW_METER_POINT),
    #     (REPLACE_MEW_METER_DEVICE, REPLACE_MEW_METER_DEVICE),
    #     (REPLACE_NEW_MODEM_OR_SIM, REPLACE_NEW_MODEM_OR_SIM),
    #     (DELETE_METER_POINT, DELETE_METER_POINT),
    #     (REPLACE_NEW_CONSTANT, REPLACE_NEW_CONSTANT),
    #     (OTHER, OTHER),
    # )

    # RESULT_OPERATION = (
    #     ('', 'Result'),
    #     (NO_COMM, NO_COMM),
    #     (YES_COMM, YES_COMM),
    #     (WAIT_COMM, WAIT_COMM),
    # )

    # LOW = 'Low'
    # MEDIUM = 'Medium'
    # HIGH = 'High'

    # VARNA = 'Varna'
    # DOBRICH = 'Dobrich'
    # SHUMEN = 'Shumen'
    # TARGOVISHTE = 'Targovishte'
    # TARNOVO = 'Veliko Tarnovo'
    # RUSE = 'Ruse'
    # RAZGRAD = 'Razgrad'
    # SILISTRA = 'Silistra'
    # GABROVO = 'Gabrovo'
    #
    # VOLTAGE = (
    #     ('', 'Voltage'),
    #     (LOW, LOW),
    #     (MEDIUM, MEDIUM),
    #     (HIGH, HIGH),
    # )
    #
    # REGIONAL_CENTER = (
    #     ('', 'Regional center'),
    #     (VARNA, VARNA),
    #     (DOBRICH, DOBRICH),
    #     (SHUMEN, SHUMEN),
    #     (TARGOVISHTE, TARGOVISHTE),
    #     (TARNOVO, TARNOVO),
    #     (RUSE, RUSE),
    #     (RAZGRAD, RAZGRAD),
    #     (SILISTRA, SILISTRA),
    #     (GABROVO, GABROVO),
    # )

    mp_name = models.CharField(
        max_length=MAX_MP_LENGTH,
        validators=(
            MinLengthValidator(MIN_MP_LENGTH),),
        unique=True,
        blank=False,
        null=False, )
    constant = models.PositiveIntegerField(
        validators=(MaxValueValidator(MAX_CONSTANT_VALUE), MinValueValidator(MIN_CONSTANT_VALUE),),
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

    created_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    modem = models.OneToOneField(
        'modems.Modem',
        related_name='modem_meter_point_key',
        to_field='modem_number',
        on_delete=models.PROTECT,
    )
    meter_device = models.OneToOneField(
        'meter_devices.MeterDevice',
        related_name='meter_device_meter_point_key',
        to_field='meter_device_number',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )
    user = models.ForeignKey(
        UserModel,
        to_field='username',
        default="Unknown",
        on_delete=models.SET_DEFAULT,
        null=True,
    )

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.db import models

from system_for_remote_meter_points.meter_points.models import MeterPoint

# Create your models here.
UserModel = get_user_model()


def validate_length(value, FIXED_MODEM_NUMBER_LENGTH):
    if len(str(value)) != FIXED_MODEM_NUMBER_LENGTH:
        raise ValidationError(u'%s is not the correct length' % value)


def only_int(value):
    if not value.isdigit():
        raise ValidationError('Contains characters')


class Task(models.Model):

    FIXED_MODEM_NUMBER_LENGTH = 6

    RESTORE_COMM = 'Възсатновяване на комуникация'
    ADD_NEW_METER_POINT = 'Добавяне на нова точка'
    REPLACE_MEW_METER_DEVICE = 'Подмяна на електромер'
    REPLACE_NEW_MODEM_OR_SIM = 'Подмяна на модем и/или СИМ карта'
    DELETE_METER_POINT = 'Изтриване на точка'
    REPLACE_NEW_CONSTANT = 'Смяна на константа'
    OTHER = 'Друго (в ,,Коментарите"")'

    NO_COMM = 'Няма комуникация'
    YES_COMM = 'Има комуникация'
    WAIT_COMM = 'В процес на изпълнение...'

    OPERATION = (
        (RESTORE_COMM, RESTORE_COMM),
        (ADD_NEW_METER_POINT, ADD_NEW_METER_POINT),
        (REPLACE_MEW_METER_DEVICE, REPLACE_MEW_METER_DEVICE),
        (REPLACE_NEW_MODEM_OR_SIM, REPLACE_NEW_MODEM_OR_SIM),
        (DELETE_METER_POINT, DELETE_METER_POINT),
        (REPLACE_NEW_CONSTANT, REPLACE_NEW_CONSTANT),
        (OTHER, OTHER),
        )

    RESULT_OPERATION = (
        (NO_COMM, NO_COMM),
        (YES_COMM, YES_COMM),
        (WAIT_COMM, WAIT_COMM),
        )

    MAX_MP_LENGTH = 50
    MIN_MP_LENGTH = 5
    MAX_CONSTANT_VALUE = 80000

    LOW = 'Ниско'
    MEDIUM = 'Средно'
    HIGH = 'Високо'

    VARNA = 'Варна'
    DOBRICH = 'Добрич'
    SHUMEN = 'Шумен'
    TARGOVISHTE = 'Търговище'
    TARNOVO = 'Велико Търново'
    RUSE = 'Русе'
    RAZGRAD = 'Разград'
    SILISTRA = 'Силистра'
    GABROVO = 'Габрово'

    VOLTAGE = (
        (LOW, LOW),
        (MEDIUM, MEDIUM),
        (HIGH, HIGH),
    )

    REGIONAL_CENTER = (
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
        unique=True,
        blank=False,
        null=False,)
    constant = models.PositiveIntegerField(
        validators=(MaxValueValidator(MAX_CONSTANT_VALUE),),
        blank=False,
        null=False,)
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
    modem_number = models.TextField(
        validators=(
            validate_length, only_int),
        unique=True,
        blank=False,
        null=False,)
    ip_address = models.GenericIPAddressField(
        null=False,
        blank=False,
    )

    operation = models.TextField(
        choices=OPERATION)
    result_operation = models.TextField(
        choices=RESULT_OPERATION)
    comment = models.TextField()


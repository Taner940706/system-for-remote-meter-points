from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.db import models



# Create your models here.
UserModel = get_user_model()


class MeterPoint(models.Model):
    MAX_MP_LENGTH = 50
    MIN_MP_LENGTH = 5
    MAX_CONSTANT_VALUE = 80000

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
    modem = models.OneToOneField(
        'modems.Modem',
        related_name='modem_meter_point_key',
        on_delete=models.PROTECT,
    )
    meter_device = models.OneToOneField(
        'meter_devices.MeterDevice',
        related_name='meter_device_meter_point_key',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.PROTECT,
    )

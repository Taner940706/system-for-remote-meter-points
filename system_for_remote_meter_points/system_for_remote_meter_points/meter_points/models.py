from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.db import models

# Create your models here.
UserModel = get_user_model()


class MeterPoint(models.Model):
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
    ip_address = models.GenericIPAddressField(
        unique=True,
        blank=False,
        null=False,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.PROTECT,
    )

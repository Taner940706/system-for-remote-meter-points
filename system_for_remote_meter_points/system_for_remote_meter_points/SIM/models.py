from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from system_for_remote_meter_points.modems.models import Modem


# Create your models here.


def validate_length(value, FIXED_GSM_NUMBER_LENGTH):
    if len(str(value)) != FIXED_GSM_NUMBER_LENGTH:
        raise ValidationError(u'%s is not the correct length' % value)


def only_int(value):
    if not value.isdigit():
        raise ValidationError('Contains characters')


class SIM(models.Model):
    MAX_SIM_NUMBER_LENGTH = 16
    MIN_SIM_NUMBER_LENGTH = 14
    FIXED_GSM_NUMBER_LENGTH = 10

    AONE = 'А1'
    YETTEL = 'Yettel'
    VIVACOM = 'Vivacom'

    OPERATOR = (
        (AONE, AONE),
        (YETTEL, YETTEL),
        (VIVACOM, VIVACOM),
    )
    sim_number = models.CharField(
        max_length=MAX_SIM_NUMBER_LENGTH,
        validators=(
            MinLengthValidator(MIN_SIM_NUMBER_LENGTH),
            only_int,),
        unique=True,
        blank=False,
        null=False,)
    gsm_number = models.TextField(
        validators=(validate_length,
                    only_int,),
        blank=False,
        null=False,)
    ip_address = models.GenericIPAddressField(
        null=False,
        blank=False,
    )
    operator = models.TextField(
        choices=OPERATOR,
        unique=True,
        null=False,
        blank=False,
    )
    
    modem = models.ForeignKey(
        Modem,
        on_delete=models.PROTECT,
    )

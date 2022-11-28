from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

def only_int(value):
    if not value.isdigit():
        raise ValidationError('Contains characters')


class Modem(models.Model):

    FIXED_MODEM_NUMBER_LENGTH = 6

    modem_number = models.CharField(
        max_length=FIXED_MODEM_NUMBER_LENGTH,
        validators=(only_int, MinLengthValidator(FIXED_MODEM_NUMBER_LENGTH),),
        unique=True,
        blank=False,
        null=False,)
    sim = models.OneToOneField(
        'SIM.SIM',
        related_name='sim_key',
        to_field='sim_number',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )





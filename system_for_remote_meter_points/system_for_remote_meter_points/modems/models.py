from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
UserModel = get_user_model()


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
    created_date = models.DateField(
        # Automatically sets current date on `save` (update or create)
        auto_now=True,
        null=False,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        to_field='username',
        on_delete=models.SET_NULL,
        null=True,
    )





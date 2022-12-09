from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
UserModel = get_user_model()


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
    gsm_number = models.CharField(
        max_length=FIXED_GSM_NUMBER_LENGTH,
        validators=(MinLengthValidator(FIXED_GSM_NUMBER_LENGTH),
                    only_int,),
        blank=False,
        null=False,)
    ip_address = models.GenericIPAddressField(
        null=False,
        blank=False,
    )
    operator = models.TextField(
        choices=OPERATOR,
        null=False,
        blank=False,
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




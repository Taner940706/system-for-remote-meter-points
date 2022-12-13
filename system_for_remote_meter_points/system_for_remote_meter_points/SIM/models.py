from enum import Enum

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from system_for_remote_meter_points.core.model_mixins import ChoicesEnumMixin
from system_for_remote_meter_points.core.validators import only_int

UserModel = get_user_model()
ANONYMOUS_USER_ID = "anonymous_user"


# meter operator choice
class Operator(ChoicesEnumMixin, Enum):
    AONE = 'А1'
    YETTEL = 'Yettel'
    VIVACOM = 'Vivacom'


class SIM(models.Model):
    MAX_SIM_NUMBER_LENGTH = 16
    MIN_SIM_NUMBER_LENGTH = 14
    FIXED_GSM_NUMBER_LENGTH = 10

    sim_number = models.CharField(
        max_length=MAX_SIM_NUMBER_LENGTH,
        validators=(
            MinLengthValidator(MIN_SIM_NUMBER_LENGTH),
            only_int,),
        unique=True,
        blank=False,
        null=False, )
    gsm_number = models.CharField(
        max_length=FIXED_GSM_NUMBER_LENGTH,
        validators=(MinLengthValidator(FIXED_GSM_NUMBER_LENGTH),
                    only_int,),
        unique=True,
        blank=False,
        null=False, )
    ip_address = models.GenericIPAddressField(
        unique=True,
        null=False,
        blank=False,
    )
    operator = models.TextField(
        choices=Operator.choices(),
        null=False,
        blank=False,
    )
    created_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )
    # foreign key for user by username if user is deleted add default anonymous user
    user = models.ForeignKey(
        UserModel,
        to_field='username',
        default=ANONYMOUS_USER_ID,
        on_delete=models.SET_DEFAULT,
        null=True,
    )

    def __str__(self):
        return self.sim_number

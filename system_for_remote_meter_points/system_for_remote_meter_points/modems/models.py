from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from system_for_remote_meter_points.core.validators import only_int

UserModel = get_user_model()
ANONYMOUS_USER_ID = "anonymous_user"


class Modem(models.Model):
    FIXED_MODEM_NUMBER_LENGTH = 6

    modem_number = models.CharField(
        max_length=FIXED_MODEM_NUMBER_LENGTH,
        validators=(only_int, MinLengthValidator(FIXED_MODEM_NUMBER_LENGTH),),
        unique=True,
        blank=False,
        null=False, )
    # one-to-one field for SIM by sim_number if modem have this sim show error 500
    sim = models.OneToOneField(
        'SIM.SIM',
        related_name='sim_key',
        to_field='sim_number',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
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
        return self.modem_number

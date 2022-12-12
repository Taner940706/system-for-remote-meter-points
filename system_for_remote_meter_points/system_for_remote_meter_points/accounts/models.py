from enum import Enum

from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_model

from system_for_remote_meter_points.core.model_mixins import ChoicesEnumMixin
from system_for_remote_meter_points.core.validators import validate_only_letters


class Department(ChoicesEnumMixin, Enum):
    DOSO = 'DOSO'
    OSP = 'OSP'
    AUDITOR = 'Auditor'
    OTHER = 'Other'


class AppUser(auth_model.AbstractUser):
    MAX_FIRST_NAME_LEN = 30
    MIN_FIRST_NAME = 4
    MAX_LAST_NAME_LEN = 30
    MIN_LAST_NAME = 4

    # DOSO = 'DOSO'
    # OSP = 'OSP'
    # AUDITOR = 'Auditor'
    # OTHER = 'Other'

    # DEPARTMENT = (
    #     (DOSO, DOSO),
    #     (OSP, OSP),
    #     (AUDITOR, AUDITOR),
    #     (OTHER, OTHER),
    # )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        validators=(
            MinLengthValidator(MIN_FIRST_NAME), validate_only_letters),
    )
    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
        validators=(
            MinLengthValidator(MIN_LAST_NAME), validate_only_letters),
    )
    email = models.EmailField()
    department = models.TextField(
        choices=Department.choices(),
        null=False,
        blank=False,
    )
    picture = models.ImageField(upload_to='user_photos/')

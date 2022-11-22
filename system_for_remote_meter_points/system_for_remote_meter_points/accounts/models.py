from django.db import models
from django.contrib.auth import models as auth_model


class AppUser(auth_model.AbstractUser):

    kid = models.CharField(
        max_length=10
    )
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=30
    )
    email = models.EmailField()
    department = models.CharField(
        max_length=30
    )
    picture = models.URLField()
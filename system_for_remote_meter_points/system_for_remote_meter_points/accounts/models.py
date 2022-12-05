from django.db import models
from django.contrib.auth import models as auth_model


class AppUser(auth_model.AbstractUser):

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
    picture = models.ImageField(upload_to='user_photos/')

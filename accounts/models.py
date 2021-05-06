from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(
        'email address',
        unique=True,
        blank=True
    )
    is_active = models.BooleanField(
        'active',
        default=False,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

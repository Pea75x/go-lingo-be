from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ENGLISH = 'en'
    SPANISH = 'es'
    LANGUAGE_CHOICES = [
        (ENGLISH, 'English'),
        (SPANISH, 'Spanish')
        # For adding more languages as the app grows
    ]
    EXPLORER = 'explorer'
    ALIEN = 'alien'
    CHARACTER_CHOICES = [
        (EXPLORER, 'Explorer'),
        (ALIEN, 'Alien')
    ]

    character = models.CharField(
        max_length=20,
        choices=CHARACTER_CHOICES,
        default=EXPLORER
    )

    target_language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default=ENGLISH,
        help_text='Language the user would like to learn',
    )

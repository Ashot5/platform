from django.core import validators
from django.db import models


class User(models.Model):
    """
        Defines our custom user class.
        Username, email and password are required.
    """
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(validators=[validators.validate_email], unique=True, blank=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    surname = models.CharField(max_length=100, blank=False, null=False)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    phone_number = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

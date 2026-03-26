from django.contrib.auth.models import AbstractUser
from django.db import models

#  Create ours models here. user = email, password, is_email_verified, created_at, updated_at

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

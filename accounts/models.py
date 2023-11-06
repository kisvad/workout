"""Module adding models for accounts app."""
from django.contrib import auth

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    """Class representing a user"""

    def __str__(self):
        return f'@{self.username}'

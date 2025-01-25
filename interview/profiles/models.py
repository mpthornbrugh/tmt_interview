"""
Add an app "profiles". The following should be a production ready model.
Create a model "UserProfile" that contains:
    username, email, password, first name, last name, date joined, last login, is staff,
    is superuser, is admin, is active.
On this model the username field should be set to use the email address for authenticating.
This model should also at minimum include functions: get_full_name(), get_username(), is_authenticated().
You should also add a field "avatar" that will contain a thumbnail image of a user's avatar.
Set the UserProfile model as the default Django user model.
"""
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class Profile(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_username(self):
        return self.username

    def is_authenticated(self):
        return self.is_active

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["-date_joined"]

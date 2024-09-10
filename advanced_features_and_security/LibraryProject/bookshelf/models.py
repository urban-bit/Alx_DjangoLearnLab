from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model, handling user and superuser creation.
    """

    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
        """
        Create and return a regular user with an email, date of birth, and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        """
        Create and return a superuser with admin rights.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, date_of_birth, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Adds additional fields: date_of_birth and profile_photo.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        # Custom permissions for managing CustomUser model instances
        permissions = [
            ("can_view", "Can view users"),
            ("can_create", "Can create users"),
            ("can_edit", "Can edit users"),
            ("can_delete", "Can delete users"),
        ]

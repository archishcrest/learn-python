from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Specify a different related name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Specify a different related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Customer(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customer_groups',  # Change the related name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customer_permissions',  # Change the related name to avoid conflict
        blank=True
    )

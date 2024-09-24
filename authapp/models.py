# models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid

class User(AbstractUser):
    ROLE_CHOICES = (
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='customer')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True, default=uuid.uuid1)
    groups = models.ManyToManyField(Group, related_name='authapp_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='authapp_user_permissions')

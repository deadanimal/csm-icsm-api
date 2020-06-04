from __future__ import unicode_literals
import json
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.postgres.fields import ArrayField
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

class CustomUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True)
    mobile_number = PhoneNumberField(blank=True)

    USER_TYPE = [
        ('AD', 'Admin'),
        ('US', 'User'),
        ('NA', 'Not Available')
    ]
    user_type = models.CharField(max_length=2, choices=USER_TYPE, default='US')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


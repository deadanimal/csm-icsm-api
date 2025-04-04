# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

class Organisation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ssm_registration_no = models.CharField(max_length=255, default='NA')
    address_line_1 = models.CharField(max_length=255, default='NA')
    address_line_2 = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=100, default='NA')
    state = models.CharField(max_length=100, default='NA')
    country = models.CharField(max_length=100, default='NA')
    ceo_name = models.CharField(max_length=100, default='NA')
    organisation_name = models.CharField(max_length=100, default='NA')
    organisation_phone = models.CharField(max_length=100, default='NA')
    organisation_email = models.CharField(max_length=100, default='NA')
    organisation_fax = models.CharField(max_length=100, default='NA')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['organisation_name']
    
    def __str__(self):
        return self.organisation_name
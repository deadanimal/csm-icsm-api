# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

class Complaint(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    COMPLAINT_TYPE = [
        ('IS', 'ICSB service'),
        ('MC', 'Misused of certificates mark'),
        ('IP', 'ISCB personal and external resources'),
        ('IC', 'ISCB client performance'),
        ('VC', 'Vulnerabilities of certified product or website'),
        ('NA', 'Not available')
    ]
    complaint_type = models.CharField(max_length=2, choices=COMPLAINT_TYPE, default='NA')
    description = models.CharField(max_length=255, default='NA')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
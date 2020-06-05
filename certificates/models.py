# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

from users.models import (
    CustomUser
)

class Certificate(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='NA')
    detail = models.CharField(max_length=255, default='NA')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class CertificateApplication(models.Model):

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
    is_large_organisation = models.BooleanField(default=False)

    ORGANISATION_TYPE = [
        ('GM', 'Government'),
        ('PM', 'Private (Malaysia)'),
        ('PF', 'Private (Foreign)'),
        ('NA', 'Not Available')
    ]
    organisation_type = models.CharField(max_length=2, choices=ORGANISATION_TYPE, default='NA')

    EMPLOYEES_AMOUNT = [
        ('1-20', '1-20'),
        ('21-50', '21-50'),
        ('51-100', '51-100'),
        ('101-200', '101-200'),
        ('> 200', 'Over 200'),
        ('NA', 'Not Available')
    ]
    employees_amount = models.CharField(max_length=2, choices=EMPLOYEES_AMOUNT, default='NA')

    TURNOVER = [
        ('< 1M', 'Less than 1 000 000'),
        ('1M-5M', '1 000 000 - 5 000 000'),
        ('5M-50M', '5 000 000 - 50 000 000'),
        ('> 50M', 'Over 50 000 000'),
        ('NA', 'Not Applicable')

    ]
    turnover = models.CharField(max_length=2, choices=TURNOVER, default='NA')
    product_name = models.CharField(max_length=100, default='NA')
    project_leader = models.CharField(max_length=100, default='NA')
    target_evaluation_name = models.CharField(max_length=100, default='NA')
    target_evaluation_description = models.CharField(max_length=100, default='NA')
    objective = models.CharField(max_length=255, default='NA')
    
    TARGET_TYPE = [
        ('AC', 'Access Control'),
        ('DS', 'Devices & Systems'),
        ('BD', 'Biometric Systems & Devices'),
        ('BP', 'Boundary Protection Devices & Systems'),
        ('DP', 'Data Protection'),
        ('DB', 'Data Bases'),
        ('DD', 'Detection Devices & Systems'),
        ('IS', 'ICs, Smart Cards and Smart Card related Devices & Systems'),
        ('KS', 'Key Management Systems')
    ]
    target_of_evaluation = models.CharField(max_length=100, default='NA')
    
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['organisation_name']
    
    def __str__(self):
        return self.organisation_name
from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from .models import (
    Certificate,
    CertificateApplication
)

class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = '__all__'

class CertificateApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CertificateApplication
        fields = '__all__'
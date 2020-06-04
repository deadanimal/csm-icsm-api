from datetime import datetime, timedelta

from django.conf import settings
from django.conf.urls import include, url
from django.contrib.gis import admin

from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from users.views import (
    MyTokenObtainPairView
)

class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

# Certificates app

from certificates.views import (
    CertificateViewSet
)

certificates_router = router.register(
    'certificates', CertificateViewSet
)

# Certificates app

from complaints.views import (
    ComplaintViewSet
)

complaints_router = router.register(
    'complaints', ComplaintViewSet
)

# Compliances app

from compliances.views import (
    ComplianceViewSet
)

compliances_router = router.register(
    'compliances', ComplianceViewSet
)

# Organisations app

from organisations.views import (
    OrganisationViewSet
)

organisations_router = router.register(
    'organisations', OrganisationViewSet
)

# Schemes app

from schemes.views import (
    SchemeViewSet
)

schemes_router = router.register(
    'schemes', SchemeViewSet
)

# Services app

from services.views import (
    ServiceViewSet
)

services_router = router.register(
    'services', ServiceViewSet
)

# Users app

from users.views import (
    CustomUserViewSet
)

users_router = router.register(
    'users', CustomUserViewSet
)

urlpatterns = [
    url(r'v1/', include(router.urls)),
    url(r'auth/', include('rest_auth.urls')),
    url(r'auth/registration/', include('rest_auth.registration.urls')),

    url('auth/obtain/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('auth/verify/', TokenVerifyView.as_view(), name='token_verify')
]
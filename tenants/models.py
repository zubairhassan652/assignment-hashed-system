from django_tenants.models import TenantMixin, DomainMixin
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)


class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    auto_create_schema = True

class Domain(DomainMixin):
    pass

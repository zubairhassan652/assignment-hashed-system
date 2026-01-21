from django.contrib import admin

from tenants.models import Domain, Tenant, User

# Register your models here.
admin.site.register(User)
admin.site.register(Tenant)
admin.site.register(Domain)
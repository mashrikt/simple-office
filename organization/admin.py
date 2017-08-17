from django.contrib import admin

from organization.models import Organization, OrganizationLink


admin.site.register(Organization)
admin.site.register(OrganizationLink)

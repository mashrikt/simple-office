from django.contrib import admin

from organization.models import Organization, OrganizationLink


class OrganizationLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'organization')

admin.site.register(Organization)
admin.site.register(OrganizationLink, OrganizationLinkAdmin)

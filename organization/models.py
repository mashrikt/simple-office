from django.conf import settings
from django.db import models


# Create your models here.
class Organization(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OrganizationLink(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True)
    organization = models.ForeignKey(Organization)
    link = models.URLField()

    def __str__(self):
        return self.title or self.link


import graphene

from graphene_django.types import DjangoObjectType

from .models import Organization, OrganizationLink


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization


class OrganizationLinkType(DjangoObjectType):
    class Meta:
        model = OrganizationLink


class Query(graphene.AbstractType):
    all_organizations = graphene.List(OrganizationType)
    all_organization_links = graphene.List(OrganizationLinkType)

    def resolve_all_organizations(self, info, **kwargs):
        return Organization.objects.all()

    def resolve_all_organization_links(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return OrganizationLink.objects.select_related('organization').all()

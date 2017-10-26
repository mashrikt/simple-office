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

    organization = graphene.Field(OrganizationType,
                              id=graphene.Int(),
                              name=graphene.String())

    organization_link = graphene.Field(OrganizationLinkType,
                                id=graphene.Int(),
                                title=graphene.String())

    def resolve_all_organizations(self, info, **kwargs):
        return Organization.objects.all()

    def resolve_all_organization_links(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return OrganizationLink.objects.select_related('organization').all()

    def resolve_organization(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Organization.objects.get(pk=id)

        if name is not None:
            return Organization.objects.get(name=name)

        return None

    def resolve_organization_link(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return OrganizationLink.objects.get(pk=id)

        if title is not None:
            return OrganizationLink.objects.get(title=title)

        return None
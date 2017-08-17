from rest_framework.serializers import ModelSerializer

from .models import Organization, OrganizationLink


class OrganizationSerializer(ModelSerializer):

    class Meta:
        model = Organization
        exclude = ('created_at',)


class OrganizationLinkSerializer(ModelSerializer):

    class Meta:
        model = OrganizationLink
        exclude = ('created_at', 'created_by', 'organization')

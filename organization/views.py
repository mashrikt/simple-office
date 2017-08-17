from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated

from organization.permissions import IsMemberOfOrganization
from organization.serializers import OrganizationSerializer, OrganizationLinkSerializer
from .models import Organization, OrganizationLink


class OrganizationList(ListAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        organization_id = self.request.user.organization.id
        queryset = Organization.objects.filter(id=organization_id)
        return queryset


class OrganizationLinkList(ListCreateAPIView):
    serializer_class = OrganizationLinkSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        organization_id = self.request.user.organization.id
        queryset = OrganizationLink.objects.filter(organization_id=organization_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organization)


class OrganizationLinkRetrieve(RetrieveDestroyAPIView):
    serializer_class = OrganizationLinkSerializer
    permission_classes = (IsMemberOfOrganization,)

    def get_queryset(self):
        organization_id = self.request.user.organization.id
        queryset = OrganizationLink.objects.filter(organization_id=organization_id)
        return queryset

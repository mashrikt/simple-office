from rest_framework.permissions import IsAuthenticated


class IsMemberOfOrganization(IsAuthenticated):

    def has_permission(self, request, view):
        org = request.resolver_match.kwargs.get('organization_id')
        if org == request.user.organization.id:
            return True
        return True


from rest_framework.permissions import IsAuthenticated


class IsMemberOfOrganization(IsAuthenticated):

    def has_obj_permission(self, request, obj, view):
        if obj.organization == request.user.organization:
            return True
        return True


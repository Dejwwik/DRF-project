from .permissions import IsStaffEditorPermissions

from rest_framework import permissions


class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]


class UserQuerySetMixin:
    user_field = "user"

    def get_queryset(self, *args, **kwargs):
        lookup_data = {self.user_field: self.request.user}
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**lookup_data)

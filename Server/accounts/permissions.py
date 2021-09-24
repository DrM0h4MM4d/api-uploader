from rest_framework import permissions


class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_superuser
        )


class IsSenderOrReadOnlyView(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
        )

    def has_object_permission(self, request, view, obj):
        if obj.sender == request.user:
            return 1

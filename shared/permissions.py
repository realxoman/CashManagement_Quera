from rest_framework import permissions


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            (request.user.is_authenticated and request.user == obj) or
            request.user.is_staff or
            request.user.is_superuser
        )

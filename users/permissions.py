from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """Class for overridding permissions to verified if user is superuser"""
    def has_permission(self, request, view):
        """is_active rights verification"""
        return request.user.is_active

    def has_object_permission(self, request, view, obj):
        """is_active rights verification"""
        return request.user.is_active

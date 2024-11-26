from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Класс для проверки доступа владельца объекта"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user if hasattr(obj, "user") else False

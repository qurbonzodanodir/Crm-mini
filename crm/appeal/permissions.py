from rest_framework import permissions


class IsOperatorOrBackOffice(permissions.BasePermission):
    def has_permission(self, request,view):
        if request.user.role == 'operator':
            return request.method in permissions.SAFE_METHODS or request.method == 'POST'
        if request.user.role == 'back_office':
            return True
        return False

    def has_object_permission(self, request,view,obj):
        if request.user.role == 'operator':
            return request.method in permissions.SAFE_METHODS
        if request.user.role == 'back_office':
            return True
        return False

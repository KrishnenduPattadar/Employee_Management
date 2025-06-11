from rest_framework import permissions

class IsHRManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'is_hr_manager', False)

class IsEmployeeAndSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            request.user == obj.user and getattr(request.user, 'is_employee', False)
        )

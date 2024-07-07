from rest_framework import permissions

class IsInvestor(permissions.BasePermission):
    def has_permission(self, request, view):
        # Define the logic to identify investors
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Investor').exists()

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Admins usually have the is_staff attribute set to True
        return request.user and request.user.is_authenticated and request.user.is_staff

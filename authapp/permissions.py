# permissions.py

from rest_framework import permissions

class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'super_admin'

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role in ['super_admin', 'admin']

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'customer'

class IsAdminOrCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.role == 'admin' or request.user.role == 'customer')        

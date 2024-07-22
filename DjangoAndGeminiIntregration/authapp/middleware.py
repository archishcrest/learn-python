# # authapp/middleware.py

# from django.shortcuts import redirect
# from django.urls import reverse
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.exceptions import AuthenticationFailed
# from .permissions import IsAdminUser, IsCustomerUser

# class RoleBasedRedirectionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(self, request, view_func, view_args, view_kwargs):
#         if not hasattr(request, 'user'):
#             return None

#         user = request.user

#         if not user.is_authenticated:
#             return None

#         view_permissions = getattr(view_func, 'cls', None).permission_classes

#         if IsAdminUser in view_permissions and not user.is_admin:
#             return redirect(reverse('customer_dashboard'))

#         if IsCustomerUser in view_permissions and not user.is_customer:
#             return redirect(reverse('admin_dashboard'))

#         return None


# authapp/middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from authapp.permissions import IsAdminUser, IsCustomerUser  # Import custom permissions

class RoleBasedRedirectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not hasattr(request, 'user'):
            return None

        user = request.user

        if not user.is_authenticated:
            return None

        # If the request is for the Django admin site, bypass this middleware
        if request.path.startswith(reverse('admin:index')):
            return None

        # Get view permissions if available
        view_permissions = getattr(view_func, 'cls', None)
        if view_permissions:
            view_permissions = getattr(view_permissions, 'permission_classes', [])

        # If view_permissions is None or empty, bypass this middleware
        if not view_permissions:
            return None

        if IsAdminUser in view_permissions and not user.is_admin:
            return redirect(reverse('customer_dashboard'))

        if IsCustomerUser in view_permissions and not user.is_customer:
            return redirect(reverse('admin_dashboard'))

        return None

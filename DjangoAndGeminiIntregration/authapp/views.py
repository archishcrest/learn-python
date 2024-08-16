# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsSuperAdmin, IsAdmin, IsCustomer

from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class SuperAdminView(APIView):
    permission_classes = [IsSuperAdmin]

    def get(self, request):
        return Response({"message": "Hello, Super Admin!"})

class AdminView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        return Response({"message": "Hello, Admin!"})

class CustomerView(APIView):
    permission_classes = [IsCustomer]

    def get(self, request):
        return Response({"message": "Hello, Customer!"})


class UserDetailsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdmin]

    def get(self, request):
        user = request.user
        user_data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.role,
        }
        return Response(user_data, status=status.HTTP_200_OK)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]


# {
#     "id": 1,
#     "username": "user1",
#     "role": "admin",
#     "email": "a@admin.com",
#     "phone_number": "123"
# }
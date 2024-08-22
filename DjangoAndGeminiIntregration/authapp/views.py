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
from django.http import JsonResponse


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    '''
    def post(self, request, *args, **kwargs):
        # Call the original post method to get the token
        response = super().post(request, *args, **kwargs)
        
        # Extract the token from the response data
        token = response.data.get('access')

        # Create a new response to set the cookie
        response = JsonResponse({'message': 'Login successful'})
        response.set_cookie(
            key='jwt', 
            value=token, 
            httponly=True,  # Make the cookie HttpOnly
            secure=True,    # Set this to True in production with HTTPS
            samesite='Lax'  # or 'Strict'
        )
        
        # You can add the refresh token in a different cookie if needed
        # refresh_token = response.data.get('refresh')
        # response.set_cookie(
        #     key='refresh_token',
        #     value=refresh_token,
        #     httponly=True,
        #     secure=True,
        #     samesite='Lax'
        # )
        
        return response
    '''

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
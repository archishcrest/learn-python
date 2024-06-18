from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import AdminSerializer
from .models import *
import bcrypt
from django.contrib.auth.hashers import check_password


class LoginView(APIView):
    def post(self, request):
    	#return Response({"message": "testing successful"}, status=status.HTTP_200_OK)
        username = request.data.get('username')
        password = request.data.get('password')
        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     #login(request, user)
        #     return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        # return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12))
        
        _user_ = AuthIdentities.objects.select_related('user').get(user__username=username)
        
        is_password_correct = check_password(password,  _user_.secret2)

        if check_password(password,  _user_.secret2):
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": is_password_correct,"msg": hashed,"msg2": _user_.secret2 }, status=status.HTTP_400_BAD_REQUEST)
        
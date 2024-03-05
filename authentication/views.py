import jwt
from django.conf import settings
from django.contrib import auth
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import LoginSerializer, UserSerializer


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get("username", "")
        password = data.get("password", "")

        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.decode({"username": user.username}, settings.JWT_SECRET_KEY)
            serializer = UserSerializer(user)
            data = {"user": serializer.data, "token": auth_token}

            return Response(data, status=status.HTTP_200_OK)

        return Response({"detail": "Inavalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

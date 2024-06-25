from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LoginSerializer
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        print("Received data for registration:", request.data)  # Debugging line
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Automatically activate the user
            user.is_active = True
            user.save()
            token = Token.objects.create(user=user)
            return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data, "token": token.key}, status=status.HTTP_201_CREATED)
        else:
            print("Registration errors:", serializer.errors)  # Debugging line
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        print("Received data for login:", request.data)  # Debugging line
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data, "token": token.key}, status=status.HTTP_200_OK)
        else:
            print("Login errors:", serializer.errors)  # Debugging line
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return HttpResponse("Welcome to the Home Page!")

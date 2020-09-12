from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer, LoginSerializer
from .models import User
from rest_framework.viewsets import ReadOnlyModelViewSet


class RegistrationAPIView(APIView):
    # Anyone can register
    permission_classes = (AllowAny,)

    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Create user if not in database
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password'),
                "email": request.data.get('email'),
                "first_name": request.data.get('first_name'),
                "last_name": request.data.get('last_name')
            }

        # Deserialize user object
        serializer = self.serializer_class(data=user)

        # Check if fields match model fields after deserializing
        serializer.is_valid(raise_exception=True)

        # If fields are valid, user object is created by calling create method in RegistrationSerializer, and then saved
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    # Anyone can login
    permission_classes = (AllowAny,)

    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password')
            }

        serializer = self.serializer_class(data=user)

        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



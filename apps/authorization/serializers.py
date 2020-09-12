####### IMPORTS #######
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User

####### SERIALIZER FOR REGISTRATION #######
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'token')

    # Calling on create_user from UserManager to create user object after serializing
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

####### SERIALIZER FOR LOGIN #######
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255, read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token')

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError('A user name is required to login')
        if password is None:
            raise serializers.ValidationError('A password is required to login')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('A user with that username or password is not found')

        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated')

        return {
            "username": user.username,
            "email": user.email,
            "token": user.token
        }
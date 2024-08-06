from rest_framework import serializers
from custom_user.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

class CreateUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'password')

    def create(self, validated):
      user = User.objects.create(
        first_name=validated['first_name'],
        last_name=validated['last_name'],
        email=validated['email'],
        password=validated['password']
      )
      return user
    
class LoginUserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField()
  password = serializers.CharField(write_only=True)

  class Meta:
     model = User
     fields = ('email', 'password')
  
  def validate(self, data):
    email = data['email']
    password = data['password']

    user = authenticate(email=email, password=password)
    if not user:
      raise ValidationError('Invalid credentials')

    refresh = RefreshToken.for_user(user)

    return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
    }

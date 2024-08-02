from rest_framework import serializers # type: ignore
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  
  password = serializers.CharField(write_only=True, required=True, max_length=60)
  password2 = serializers.CharField(write_only=True, required=True, max_length=60)

  class Meta:
    model = User
    fields = ['email', 'first_name', 'last_name', 'password', 'password2']

    def validate(self, attrs):
       password = attrs.get('password', '')
       password2 = attrs.get('password2', '')
       if password!= password2:
          raise serializers.ValidationError('password do not match')
       return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
           email=validated_data['email'],
           first_name=validated_data['first_name'],
           last_name=validated_data['last_name'],
           password=validated_data['password']
        )
        # Use the UserManager's create_user method to create the user
        return user
    
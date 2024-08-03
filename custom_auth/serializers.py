from rest_framework import serializers # type: ignore
from custom_auth.models import User

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['email', 'first_name', 'last_name', 'password']

   #  def validate(self, attrs):
   #    password = attrs.get('password', '')
   #    password2 = attrs.get('password2', '')
   #    if password != password2:
   #       raise serializers.ValidationError('password do not match')
   #    return attrs

    def create(self, **validated_data):
      user = User.userObject.create_user(
         email=validated_data['email'],
         first_name=validated_data.get('first_name'),
         last_name=validated_data.get('last_name'),
         password=validated_data.get('password')
      )
        # Use the UserManager's create_user method to create the user
      return user
    
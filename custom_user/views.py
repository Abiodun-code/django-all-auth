from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from custom_user.serializers import CreateUserSerializer, LoginUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class CreateUserView(GenericAPIView):
  serializer_class = CreateUserSerializer
  permission_classes = [AllowAny]

  def post(self, request):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class LoginUserView(TokenObtainPairView):
  serializer_class = LoginUserSerializer
  permission_classes = [AllowAny]

  def post(self, request):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
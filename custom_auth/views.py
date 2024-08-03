from .utils import sendOtp
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import UserSerializer

User = get_user_model()

class RegisterView(GenericAPIView):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
      user_data = request.data
      serializer = self.serializer_class(data=user_data)
      if serializer.is_valid(raise_exception=True):
         
         user=serializer.save()
        #  sendOtp(user['email'])
        #  send email function user['email']
      return Response(status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
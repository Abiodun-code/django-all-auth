from .utils import sendOtp
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import UserSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
      user_data = request.data
      serializer = self.serializer_class(data=user_data)
      if serializer.is_valid():
         serializer.save()
         user=serializer.data
         sendOtp(user['email'])
        #  send email function user['email']
      return Response({
        'user': user
      }, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
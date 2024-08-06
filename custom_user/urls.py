from django.urls import path, include
from custom_user.views import CreateUserView, LoginUserView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('refresh/',TokenRefreshView.as_view(), name='refresh'),
]
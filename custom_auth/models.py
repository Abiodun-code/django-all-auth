from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
  
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  # REQUIRED_FIELDS = ['first_name', 'last_name']

  userObject = UserManager()

  def __str__(self):
    return self.email
  
  def tokens(self):
    pass


class OneTimePassword(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  code = models.CharField(max_length=6, unique=True)

  def __str__(self):
    return f'{self.user.first_name} {self.user.last_name} passcode'
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from custom_user.managers import UserManager

# Create your models here.

class User(AbstractBaseUser):
  first_name = models.CharField(max_length=50, verbose_name=(_('First Name')))
  last_name = models.CharField(max_length=50, verbose_name=(_('Last Name')))
  email = models.EmailField(unique=True, verbose_name=(_('Email Address')))
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ('first_name', 'last_name')

  objects = UserManager()

  def __str__(self) -> str:
    return self.email
  
  def has_module_perms(self, perm, obj=None):
    return self.is_admin
  
  def has_perm(self, perm, obj=None):
    return self.is_admin
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
  def create_user(self, first_name, last_name, email, password, **extra_fields):

    if not email:
      raise ValueError(_("Please provide an email address"))
    
    if not first_name:
      raise ValueError(_("Please provide a first name"))
    
    if not last_name:
      raise ValueError(_("Please provide a last name"))
    
    email = self.normalize_email(email)
    user = self.model(first_name=first_name, last_name=last_name, email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, first_name, last_name, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_admin', True)

    if not extra_fields.get('is_staff', True):
      raise ValueError(_('Superuser must have is_staff=True.'))
    
    if not extra_fields.get('is_admin', True):
      raise ValueError(_('Superuser must have is_admin=True.'))
    
    user = self.create_user(first_name, last_name, email, password, **extra_fields)
    user.save(using=self._db)
    return user
  
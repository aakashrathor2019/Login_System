from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
  use_in_migrations=True

  def create_user(self,phone_number,password=None,**extra_fields):
     if not phone_number:
        raise ValueError('phone no is required')
     phone_number=self.normalize_phone_number(phone_number)
     user=self.model(phone_number=phone_number,**extra_fields)
     user.set_password(password)
     user.save(using=self.db)

     return user
  
  def create_superuser(self,phone_number,password=None,**extra_fields):
     extra_fields.setdefault('is_staff',True)
     extra_fields.setdefault('is_active',True)
     extra_fields.setdefault('is_superuser',True)

     if extra_fields.get('is_staff') is not True:
        raise ValueError('SuperUser is must is_staff=True')
     if extra_fields.get('is_active') is not True:
        raise ValueError('SuperUser  is must is_staff=True')
     
     return self.create_user(phone_number,password,**extra_fields)
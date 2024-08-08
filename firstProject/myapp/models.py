from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=200, default='', blank=True)
    last_name=models.CharField(max_length=100, null=True,default='')
    

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number
    
class Customer(models.Model):
    user_type=[
        ('admin','Admin'),
        ('director','director'),
        ('co-admin','co-admin'),
    ]
    userType=models.CharField(max_length=50,choices=user_type)
    firstname=models.CharField(max_length=100,null=False,unique=True)
    lastname=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.firstname}"
    
class Student(models.Model):
    phone_number=models.CharField(max_length=20)
    password=models.CharField(max_length=50)
    username=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.username}"
    

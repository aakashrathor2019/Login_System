from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import Customer,CustomUser,Student

 
admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(Student)
from django.contrib import admin

# Register your models here.
from . models import *

@admin.register(UserRegister)
class UserRgisterAdmin(admin.ModelAdmin):
    fields = ['firstname','lastname','email','gender','password']
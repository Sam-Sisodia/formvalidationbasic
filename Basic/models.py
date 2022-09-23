
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def lenpassword(value):
    if len(value) < 4 :
        raise ValidationError("Password is to short ")

class UserRegister(models.Model):
    firstname = models.CharField(max_length=12)
    lastname = models.CharField(max_length=12)
    email = models.EmailField()
    gender = models.CharField(max_length=12,null=True, blank=True)
    password = models.CharField(max_length=12 ,validators=[lenpassword])
    


    
from django.db import models
from django.contrib.auth.models import AbstractUser

class Customuser(AbstractUser):
    ROLE_CHOICES = [
        ('operator','Operator'),
        ('back_office','Back Office')
    ]
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='operator')

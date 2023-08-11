from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    TENANT = 1
    VIGILANT = 2
    
    ROL_CHOICES = (
        (TENANT,'inquilino'),
        (VIGILANT,'Vigilante')
    )
    
    role=models.PositiveSmallIntegerField(choices=ROL_CHOICES, blank=True, null=True)
    email= models.EmailField(unique=True)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['username']
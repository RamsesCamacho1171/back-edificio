from django.db import models
from users.models import User

# Create your models here.
class Department(models.Model):
    
    FIRST = 1
    SECOND = 2
    THIRD = 3
    
    ROL_CHOICES = (
        (FIRST,'Primer piso'),
        (SECOND,'Segundo piso'),
        (THIRD,'Tercer piso'),
    )
    
    num_department = models.BigAutoField(primary_key=True)
    floor = models.PositiveSmallIntegerField(choices=ROL_CHOICES)
    #se pone aqui la relacion porque un inquilino puede llegar a poseer uno o mas departamentos
    tenant=models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
from django.db import models
from users.models import User
# Create your models here.

class Tenant(models.Model):
    num_tenant = models.BigAutoField(primary_key=True)
    info_user=models.OneToOneField(
        User,
        on_delete= models.CASCADE
    )
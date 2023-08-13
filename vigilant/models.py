from django.db import models
from users.models import User
# Create your models here.

class Vigilant(models.Model):
    num_vigilant = models.BigAutoField(primary_key=True)
    info_user=models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
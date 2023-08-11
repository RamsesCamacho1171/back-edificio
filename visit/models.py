from django.db import models
from departments.models import Department
# Create your models here.

class Visit(models.Model):
    num_visit=models.BigAutoField(primary_key=True)
    department=models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    is_active=models.BooleanField()
    token=models.CharField(max_length=20, blank=True, null=True)
    date_registration = models.DateField(auto_now=True)
    entry_date=models.DateField(blank=True,null=True)
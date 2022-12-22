from django.db import models

from patients.models import RegisterUser


# Create your models here.
class RegisterAppointment(models.Model):
    patients = models.ForeignKey(RegisterUser, related_name='appointments', on_delete=models.CASCADE)
    disease = models.CharField(max_length=500)
    date = models.DateField()
    timings = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

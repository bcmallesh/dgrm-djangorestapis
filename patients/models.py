from django.db import models


# Create your models here.
class RegisterUser(models.Model):
    user_name = models.CharField(max_length=500)
    user_email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    user_dob = models.DateField()
    location = models.CharField(max_length=500)
    user_mobile = models.CharField(max_length=500)


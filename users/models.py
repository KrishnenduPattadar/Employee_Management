from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_hr_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=True)

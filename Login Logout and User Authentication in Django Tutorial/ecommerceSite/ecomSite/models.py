from django.db import models
from django.contrib.auth.models import User


class SiteUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()

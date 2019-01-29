from django.db import models

# Create your models here.

class UserAccount(models.Model):
   password = models.CharField(max_length=200)
   account_number = models.CharField(max_length=100)
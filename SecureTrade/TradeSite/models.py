from django.db import models

# Create your models here.

class UserAccount(models.Model):
   password = models.CharField(max_length=200)
   account_number = models.CharField(max_length=100)


class TransactionHistory(models.Model):
   sender = models.CharField(max_length=200)
   receiver = models.CharField(max_length=100)
   transaction_date = models.DateTimeField('transaction date')
   amount = models.CharField(max_length=100)

   def __str__(self):
      return self.sender
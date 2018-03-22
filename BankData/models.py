from __future__ import unicode_literals
from django.core.validators import MinValueValidator
from django.db import models

# Model holding transaction data.


class Transaction(models.Model):
    details = models.CharField(max_length=20)
    postingDate = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    amount = models.FloatField()
    type = models.CharField(max_length=30)
    balance = models.FloatField()
    checkOrSlipNum = models.CharField(max_length=20)


#  Model holding maximum budget.


class BudgetAmount(models.Model):
    amount = models.FloatField(validators=[MinValueValidator(0)])


# Model holding budget categories and allocated amounts


class BudgetCategory(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField(validators=[MinValueValidator(0)])

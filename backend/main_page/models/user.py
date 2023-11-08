from django.db import models

from main_page.models.accounts import Accounts

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    accounts = models.OneToOneField(Accounts, on_delete=models.CASCADE, null=True)

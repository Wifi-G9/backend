from django.db import models

from main_page.models.Accounts import Accounts


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_lenght=100)
    age = models.IntegerField()
    email = models.CharField(max_lenght=100, unique=True)
    password = models.CharField(max_lenght=100)
    accounts = models.OneToOneField(Accounts, on_delete=models.CASCADE, null=True)

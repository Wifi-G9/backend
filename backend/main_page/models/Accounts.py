from django.db import models


class Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    instagram_access_token = models.CharField(max_length=100)
    twitter_access_token = models.CharField(max_length=100)
    facebook_access_token = models.CharField(max_length=100)

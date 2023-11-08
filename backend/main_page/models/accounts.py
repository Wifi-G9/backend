from django.db import models


class Accounts(models.Model):
    instagram_access_token = models.CharField(max_length=100)
    twitter_access_token = models.CharField(max_length=100)
    facebook_access_token = models.CharField(max_length=100)

from django.db import models

from django.db import models

class WordHistory(models.Model):

    word = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

from django.db import models

from backend.user_page.models.User import User


class DeveloperMessages(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_lenght=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

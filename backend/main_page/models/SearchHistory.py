from django.db import models

from main_page.models.User import User


class SearchHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    search_query = models.CharField(max_lenght=100)

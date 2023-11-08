from django.db import models

from main_page.models.user import User


class SearchHistory(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)
    search_query = models.CharField(max_length=100)

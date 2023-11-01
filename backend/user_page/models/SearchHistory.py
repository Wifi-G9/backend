from django.db import models

from backend.user_page.models.User import User


class SearchHistory(models.Models):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    search_query = models.CharField(max_lenght=100)


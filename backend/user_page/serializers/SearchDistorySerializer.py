from rest_framework import serializers

from backend.user_page.models.SearchHistory import SearchHistory


class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = '__all__'
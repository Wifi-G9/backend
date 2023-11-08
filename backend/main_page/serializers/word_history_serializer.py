from rest_framework import serializers

from main_page.models.word_history import WordHistory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordHistory
        fields = '__all__'

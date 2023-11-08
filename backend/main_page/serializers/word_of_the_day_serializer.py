from rest_framework import serializers

from main_page.models.word_of_the_day import WordOfTheDay


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordOfTheDay
        fields = '__all__'

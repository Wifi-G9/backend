from rest_framework import serializers

from main_page.models.DeveloperMessage import DeveloperMessage


class DeveloperMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeveloperMessage
        fields = '__all__'

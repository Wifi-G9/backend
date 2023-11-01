from rest_framework import serializers

from backend.user_page.models.User import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
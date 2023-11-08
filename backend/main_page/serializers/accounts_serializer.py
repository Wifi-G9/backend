from rest_framework import serializers

from main_page.models.Accounts import Accounts


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'

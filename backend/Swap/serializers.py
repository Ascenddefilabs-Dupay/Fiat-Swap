from rest_framework import serializers

from .models import AdminCMS
class AdminCMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminCMS
        fields = ['account_type', 'currency_type','icon'] 
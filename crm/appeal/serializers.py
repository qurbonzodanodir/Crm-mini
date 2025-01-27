from rest_framework import serializers
from .models import Appeal

class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['id', 'customer_name', 'account_number','phone_number', 'status', 'assigned_to','comment', 'created_at', 'photo']
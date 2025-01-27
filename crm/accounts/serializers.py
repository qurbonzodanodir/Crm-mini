from rest_framework import serializers
from .models import Customuser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ['id', 'username', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Customuser(
            username=validated_data['username'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password']) 
        user.save()
        return user

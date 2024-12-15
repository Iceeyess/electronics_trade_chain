from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        """Переопределенный класс для шифрования пароля"""
        user = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

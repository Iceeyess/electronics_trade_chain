from rest_framework import serializers

from trade.models import TradeCompany
from rest_framework.serializers import ValidationError

class TradeCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeCompany
        fields = '__all__'

    def create(self, validated_data):
        if validated_data.supplier_ending_balance:
            raise ValidationError(f"Нельзя создавать данные с остатками взаиморасчетов")
        return super().create(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('supplier_ending_balance'):
            raise ValidationError(f"Нельзя Обновлять данные с остатками взаиморасчетов")
        return super().update(instance, validated_data)
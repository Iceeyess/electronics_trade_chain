from rest_framework import serializers
from trade.models import TradeCompany
from trade.validators import CrossOffSupplierEndingBalance


class TradeCompanySerializer(serializers.ModelSerializer):
    """Сериализатор для Представления TradeCompanyModelViewSet и TradeFilterListView"""
    supplier_ending_balance = serializers.FloatField(validators=[CrossOffSupplierEndingBalance()])

    class Meta:
        model = TradeCompany
        fields = '__all__'

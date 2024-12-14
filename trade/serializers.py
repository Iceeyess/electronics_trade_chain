from rest_framework import serializers

from trade.models import TradeCompany
from rest_framework.serializers import ValidationError

from trade.validators import CrossOffSupplierEndingBalance


class TradeCompanySerializer(serializers.ModelSerializer):
    supplier_ending_balance = serializers.FloatField(validators=[CrossOffSupplierEndingBalance()])
    class Meta:
        model = TradeCompany
        fields = '__all__'

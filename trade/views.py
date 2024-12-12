from django.shortcuts import render
from rest_framework import viewsets

from trade.models import TradeCompany
from trade.serializers import TradeCompanySerializer


# Create your views here.
class TradeCompanyModelViewSet(viewsets.ModelViewSet):
    queryset = TradeCompany
    serializer_class = TradeCompanySerializer
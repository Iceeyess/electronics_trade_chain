from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from trade.models import TradeCompany
from trade.serializers import TradeCompanySerializer


# Create your views here.
class TradeCompanyModelViewSet(viewsets.ModelViewSet):
    queryset = TradeCompany
    serializer_class = TradeCompanySerializer

class TradeFilterListView(generics.ListAPIView):
    queryset = TradeCompany.objects.all()
    serializer_class = TradeCompanySerializer
    filter_backends = (SearchFilter, )
    search_fields = ('contact__country', )
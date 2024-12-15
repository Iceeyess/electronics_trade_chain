from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from trade.models import TradeCompany
from trade.serializers import TradeCompanySerializer
from .permissions import IsActive


# Create your views here.
class TradeCompanyModelViewSet(viewsets.ModelViewSet):
    queryset = TradeCompany.objects.all()
    serializer_class = TradeCompanySerializer
    permission_classes = (IsActive, )

class TradeFilterListView(generics.ListAPIView):
    queryset = TradeCompany.objects.all()
    serializer_class = TradeCompanySerializer
    filter_backends = (SearchFilter, )
    search_fields = ('contact__country', )
from trade import views
from trade.apps import TradeConfig
from rest_framework.routers import DefaultRouter
from django.urls import path


app_name = TradeConfig.name

router = DefaultRouter()
router.register(r'supplier', views.TradeCompanyModelViewSet, basename='supplier')
urlpatterns = [
    # search API
    path('search/', views.TradeFilterListView.as_view(), name='search_trade_companies'),
] + router.urls

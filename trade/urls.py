from trade import views
from trade.apps import TradeConfig
from trade.models import TradeCompany
from rest_framework.routers import DefaultRouter

app_name = TradeConfig.name

router = DefaultRouter()
router.register(r'supplier', views.TradeCompanyModelViewSet, basename='supplier')
urlpatterns = [

] + router.urls

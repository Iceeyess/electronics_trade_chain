from django.contrib import admin

from trade.models import TradeCompany

# Register your models here.
admin.site.header = 'Админка'


admin.site.register(TradeCompany)
class AdminTradeCompany(admin.ModelAdmin):
    list_display = ('supplier__name', )
    list_filter = ('contact__city', )
    
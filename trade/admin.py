from django.contrib import admin

from trade.models import TradeCompany, Contact, Product

# Register your models here.
admin.site.site_header = 'Управление поставщиками'


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('pk', 'email', 'city', )
    list_filter = ('country', 'city', 'street')


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_model', 'release_date', 'trade_company__name')
    list_filter = ('name', 'brand', 'trade_company__name')
    search_fields = ('id', 'name', 'product_model')


@admin.register(TradeCompany)
class AdminTradeCompany(admin.ModelAdmin):
    list_display = ('pk', 'name', 'supplier__name', 'supplier_ending_balance')
    list_display_links = ('supplier__name', )
    list_filter = ('contact__city', )
    ordering = ('name', )
    actions = ('set_null_to_ending_balance', )

    @admin.action(description='Обнулить задолженность')
    def set_null_to_ending_balance(self, request, queryset):
        queryset.update(supplier_ending_balance=0)
        self.message_user(request, "Задолженности перед поставщиками успешно обнулены.")



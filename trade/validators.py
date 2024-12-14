from rest_framework.serializers import ValidationError


class CrossOffSupplierEndingBalance:
    """Данный класс убирает/вычеркивает возможность обновлять поле supplier_ending_balance.
    Ответ сервера будет кастомный"""
    def __call__(self, value):
        if value is not None:
            raise ValidationError(f"Нельзя создавать данные с остатками взаиморасчетов")
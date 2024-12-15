from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.
NULLABLE = dict(null=True, blank=True)


class Contact(models.Model):
    email = models.EmailField(max_length=150, verbose_name='электронная почта')
    country = models.CharField(max_length=250, verbose_name='страна')
    city = models.CharField(max_length=250, verbose_name='город')
    street = models.CharField(max_length=250, verbose_name='улица')
    house = models.CharField(max_length=40, verbose_name='дом')

    def __str__(self):
        return f'{self.email}, {self.country}, {self.city}, {self.street}, {self.house}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Product(models.Model):
    name = models.CharField(max_length=250, help_text='введите наименование продукта',
                            verbose_name='наименование продукта')
    brand = models.CharField(max_length=150, verbose_name='торговая марка', **NULLABLE)
    product_model = models.CharField(max_length=250, help_text='введите модель', unique=True,
                                     verbose_name='название модели',  **NULLABLE)
    release_date = models.DateField(help_text='дата выпуска продукта в продажу', verbose_name='Дата выпуска продукта',
                                    **NULLABLE)
    trade_company = models.ForeignKey('TradeCompany', on_delete=models.SET_NULL, verbose_name='компания', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.product_model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class TradeCompany(models.Model):
    name = models.CharField(max_length=250, help_text='Название компании')
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, verbose_name='ссылка на контакты', **NULLABLE)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='поставщик', **NULLABLE)
    supplier_ending_balance = models.FloatField(default=0, verbose_name='задолженность перед поставщиком')
    creation_time = models.TimeField(auto_now_add=True, verbose_name='время создания')

    def clean(self):
        if self.supplier_ending_balance < 0:
            raise ValidationError('Задолженность не может быть отрицательной.')
        if self.supplier == self:
            raise ValidationError('Компания не может быть поставщиком для себя.')
        if len(re.split(r'[ ,.]', str(self.supplier_ending_balance))[1]) > 2:
            raise ValidationError('Допустимое число знаков после запятой в задолженности - 2.')
        return self

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'
        ordering = ('name', )

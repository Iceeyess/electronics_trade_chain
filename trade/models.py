from django.db import models

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


class Product(models.Model):
    name = models.CharField(max_length=250, help_text='введите наименование продукта',
                            verbose_name='наименование продукта')
    product_model = models.CharField(max_length=250, help_text='введите модель', unique=True, verbose_name='название модели')
    release_date = models.DateField(help_text='дата выпуска продукта в продажу', verbose_name='Дата выпуска продукта')

    def __str__(self):
        return f'{self.name} - {self.product_model}'

class TradeCompany(models.Model):
    name = models.CharField(max_length=250, help_text='Название компании')
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, verbose_name='ссылка на контакты', **NULLABLE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='ссылка на контакты', **NULLABLE)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='поставщик', **NULLABLE)
    supplier_ending_balance = models.FloatField(default=0, verbose_name='задолженность перед поставщиком')
    creation_date = models.TimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

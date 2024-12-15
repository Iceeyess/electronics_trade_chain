# Generated by Django 5.1.4 on 2024-12-15 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, verbose_name='электронная почта')),
                ('country', models.CharField(max_length=250, verbose_name='страна')),
                ('city', models.CharField(max_length=250, verbose_name='город')),
                ('street', models.CharField(max_length=250, verbose_name='улица')),
                ('house', models.CharField(max_length=40, verbose_name='дом')),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
            },
        ),
        migrations.CreateModel(
            name='TradeCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название компании', max_length=250)),
                ('supplier_ending_balance', models.FloatField(default=0, verbose_name='задолженность перед поставщиком')),
                ('creation_date', models.TimeField(auto_now_add=True, verbose_name='дата создания')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trade.contact', verbose_name='ссылка на контакты')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trade.tradecompany', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'компания',
                'verbose_name_plural': 'компании',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='введите наименование продукта', max_length=250, verbose_name='наименование продукта')),
                ('brand', models.CharField(blank=True, max_length=150, null=True, verbose_name='торговая марка')),
                ('product_model', models.CharField(blank=True, help_text='введите модель', max_length=250, null=True, unique=True, verbose_name='название модели')),
                ('release_date', models.DateField(blank=True, help_text='дата выпуска продукта в продажу', null=True, verbose_name='Дата выпуска продукта')),
                ('trade_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trade.tradecompany', verbose_name='компания')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]

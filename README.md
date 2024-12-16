В данном задании вам предлагается разработать онлайн платформу-торговой сети электроники

Общая информация
------------------------------------------------------------------------------------------------------------------------
Тестовое задание состоит из нескольких задач. Мы примем вашу кандидатуру к рассмотрению только в том случае, если работа
выполнена целиком. Попытайтесь продемонстрировать ваш уровень опыта и навыков в каждой задаче, чтобы мы смогли в полной
мере оценить вашу кандидатуру.
Вы должны отправить ваше готовое приложение в виде ссылки на GitHub- или GitLab-репозиторий. Если вы пришлете приложение
в любом другом виде (в виде ссылки на zip-архив, прикрепите zip-архив к письму и др.), ваша кандидатура не будет нами
рассмотрена!
Если вы сделали не все пункты тестового задания — пожалуйста, укажите причину, по которой вы их не выполнили (не хватило
времени, не хватило опыта/знаний, что-то еще).
Технические требования

- Python 3.8+
- Django 3+
- DRF 3.10+
- PostgreSQL 10+
  При выполнении тестового задания вы можете дополнительно использовать любые сторонние Python-библиотеки без всяких
  ограничений.

Задание
- Создайте веб-приложение с API-интерфейсом и админ-панелью.
- Создайте базу данных, используя миграции Django.

Требования к реализации:

1) Необходимо реализовать модель сети по продаже электроники.
Сеть должна представлять собой иерархическую структуру из трех уровней:

- завод;
- розничная сеть;
- индивидуальный предприниматель.
Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т. е. завод всегда находится на уровне 0, а если розничная сеть относится напрямую к заводу, минуя остальные звенья, ее уровень — 1.
------------------------------------------------------------------------------------------------------------------------
2) Каждое звено сети должно обладать следующими элементами:

а)Название. 

б)Контакты:
- email,
- страна,
- город,
- улица,
- номер дома.

в)Продукты:
- название,
- модель,
- дата выхода продукта на рынок.

г)Поставщик (предыдущий по иерархии объект сети).

д)Задолженность перед поставщиком в денежном выражении с точностью до копеек.

е)Время создания (заполняется автоматически при создании).

------------------------------------------------------------------------------------------------------------------------
3) Сделать вывод в админ-панели созданных объектов.
На странице объекта сети добавить:

- ссылку на «Поставщика»;
- фильтр по названию города;
- admin action, очищающий задолженность перед поставщиком у выбранных объектов.

------------------------------------------------------------------------------------------------------------------------

4) Используя DRF, создать набор представлений:
- CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»).
- Добавить возможность фильтрации объектов по определенной стране.

------------------------------------------------------------------------------------------------------------------------

5) Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.

------------------------------------------------------------------------------------------------------------------------
Реализация
------------------------------------------------------------------------------------------------------------------------

Для реализации проекта было принято решение в формировании одного приложения trade, в котором вся реализация. 
Приложение users не стал устанавливать, поскольку не было веских причин в кастомизации пользователей.
Для взаимодействия выбрал способ создания пользователей и прочие работы с пользовательскими моделями через приложение 
djoser. 
Документация на здание пользователя:
https://djoser.readthedocs.io/en/latest/base_endpoints.html#user-create
Там же можно найти и прочие взаимодействия с пользователем и полный CRUD.

- Клонируйте проект из github репозитория, создайте виртуальную среду, войдите в виртуальную среду.
- Установите зависимости через команду python3 install -r requirements.txt
- Выполните подключение к БД используя шаблон из .env.example файла
- Проверьте подключение к БД через python3 manage.py runserver, если выдаст ошибку, устраните ее,пока не подключитесь 
к БД.
- Выполните миграции через python3 manage.py migrate
- Загрузите фикстуры по ранее созданным тестовым моделям торговых компаний, контактов и продуктов через:
python3 manage.py loaddata trade.json


Для того, чтобы войти в админку, необходимо:

1) Создать пользователя.
URL:
http://localhost:8000/api/v1/auth/users/

2) Можете пропустить пункт и, сразу же пойти в пункт 3, но, можно активировать аккаунт пользователя посредством 
встроенных djoser API.
Сразу же, после успешного выполнения, найдите папку sending_email_log, в ней будет файл, например 
20241216-183832-124031847424240.log , в нем будет ссылка активации с uid, и token. Пример ссылки:
http://localhost:8000/#/activate/MQ/ci5548-a53c0d31c6b1c2fad85232a74ed2cd16 . 
uid: MQ
token: ci5548-a53c0d31c6b1c2fad85232a74ed2cd16
Затем необходимо пройти по ссылке http://localhost:8000/api/v1/auth/users/activation/ с методом POST:
с параметрами в теле запроса:
uid: MQ
token: ci5548-a53c0d31c6b1c2fad85232a74ed2cd16
Проверьте в БД, поле is_active должно стать true.

Ссылка получения токена:
http://localhost:8000/auth/token/login
Метод: POST
{
    "password": "sample",
    "username": "sample"
}
, где sample - ваши данные.

Пройдите по ссылке API с методом PATCH:
http://localhost:8000/api/v1/auth/users/me/
{
    "is_staff": true
}
Добавьте в headers:
- Authorization
- Token 1d2904e355beced1507327fc288522ba9414c213
Номер токена получите собственный, выше токен для примера.

Суперпользователя можете уже либо изменить через ORM запросы в python.manage.py shell, либо в самой БД.

Например, в ORM:

python manage.py shell

from django.contrib.auth.models import User

u = User.objects.get(username='your_username')

u.is_superuser = True

u.save()


3) Наделить его полномочиями суперпользователя.
Можно через БД, поставить true для полей: is_superuser, is_staff, is_active.

Таким образом, можно протестировать загруженные фикстуры через http://localhost:8000/admin/

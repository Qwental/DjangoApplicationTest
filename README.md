Просто интерент магазин по курсу с ютуба
Создать фикстуру правильно:
python -Xutf8 manage.py dumpdata products.Product -o goods.json
python -Xutf8 manage.py dumpdata products.Product -o categories.json


Запуск приложения
1 Установи зависимости: pip install -r requirements.txt
2 Выполни миграцию для БД - python manage.py migrate
3 Создай админ-аккаунт (с ним ты войдешь в админку Django) - python manage.py createsuperuser
4 Заполни БД данными - 

python manage.py loaddata .\products\fixtures\goods.json
python manage.py loaddata .\products\fixtures\categories.json

5 Запуск приложения производиться всегда этой командой python manage.py runserver и перейди на http://127.0.0.1:8000/

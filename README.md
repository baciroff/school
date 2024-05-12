# Установка

1. Клонируйте репозиторий
```
https://github.com/
```
Если вы не используете Git, то вы можете просто скачать исходный код репозитория в ZIP-архиве и распаковать его на свой компьютер.

2. Создайте виртуальное окружение и активируйте его
```
python -m venv venv
source venv/bin/activate
```
3. Установите зависимости
```
pip install django
```
4. Запустите миграции и загрузите данные в БД
```
python manage.py migrate
python manage.py loaddata db.json
```
5. Создайте администратора магазина
```
python manage.py createsuperuser
```
6. Запустите сервер
```
python manage.py runserver
```

# Готово!
Вы успешно установили проект на Django и готовы начать его использовать!
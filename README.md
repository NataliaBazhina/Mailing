Сервис управления рассылками

 — это веб-приложение для управления рассылками, созданное с использованием Django. 
Сервис предоставляет возможность создавать письма, рассылать их клиентами, отслеживать попытки рассылок.
Основные возможности:

    Отправка немедленной рассылки  через интерфейс пользователя и командную строку(python manage.py send_last_mailing)
    Отправка запланированной рассылки с заданной переодичностью. 

Сущности системы:
    
    Клиенты: Получатели рассылок с полями для контактных данных.
    Рассылка: Рассылка сообщений с параметрами .
    Письмо: Тема и тело письма для рассылки.
    Попытка рассылки: Запись о статусе попытки отправки сообщения.
    Пользователи: Создатели рассылок. 

На главной странице отображается общее количество рассылок, число актуальных клиентов и активных рассылок. 

Доработка сервиса:

    Блог: Создание блога для продвижения сервиса с функциями управления статьями (заголовок, содержимое, количество просмотров).
    Кеширование: Настройка кеширования для страницы рассылок и детальной информации о рассылке.
    Контроль доступа: Разграничение прав доступа для разных типов пользователей, ограничение редактирования рассылок и клиентов.
    Регистрация и аутентификация пользователей
    Статистика рассылок.

Технологии:

    Django: Веб-фреймворк, используемый для разработки бэкенда.
    PostgreSQL: Система управления базами данных, используемая для хранения данных приложения.
    UIkit Bootstrap: Фреймворк для интерфейса.
    APScheduler: Используется для работы с периодическими задачами.
    Redis: Используется для кеширования с целью повышения производительности и ускорения извлечения данных.

Запуск:
Установка и настройка
1. Клонировать репозиторий

Сначала клонируйте репозиторий с GitHub:

https://github.com/NataliaBazhina/Mailing.git
cd mailing

2. Создать и активировать виртуальное окружение

Создайте виртуальное окружение с помощью `venv` и активируйте его:

Для Linux/macOS:

```bash
python3 -m venv env
source env/bin/activate

Для Windows:
python -m venv env
.\env\Scripts\activate

3. Установить зависимости

Установите зависимости из файла requirements.txt:
pip install -r requirements.txt

4. Запустить миграции

После установки зависимостей выполните миграции для базы данных:

python3 manage.py migrate

5. Создать суперпользователя

Для создания суперпользователя выполните команду:
python3 manage.py createsuperuser


Для запуска сервера выполните команду:
python3 manage.py runserver

Сервер будет доступен по адресу: http://127.0.0.1:8000
# Тестовый проект - песочница (backend)
## Описание
...
## Установка
- Инициализируем локальный репозиторий и скачиваем проект:
    ```bash
  git init
  git clone https://github.com/woodenowl/backend_portal.git
    ```
- Переходим в каталог с проектом и создаем виртуальное окружение:
    ```bash
  cd backend_portal
  python -m venv venv
  venv/Scripts/activate
    ```
- Устанавливаем пакеты:
    ```bash
  pip install -r requirements.txt
    ```
- Не забываем установить redis:
    - Скачиваем zip [отсюда](https://github.com/microsoftarchive/redis/releases/tag/win-3.2.100)
    - Запускаем ```redis-server.exe```
    - Запускаем ```redis-cli.exe```
    - Пишем во второй консоли ```ping```, если верулось ```PONG```, то всё окей
- The end

## Стек технологий
**Back**\
django, Rest API, Postgresql, Celery, Redis

**Front**\
html, css, js, Vue

**Host**\
localhost :)

## Контакты
- mail: il.nordsky@gmail.com
- vk: [Ilya Basisty](https://vk.com/ilnord)

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)

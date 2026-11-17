# Скрипт загрузки контента по переданному URL.

### Установка

В unix системах:
```
git clone https://github.com/CaDiBob/download_url.git && cd download_url
```
В Windows (cmd или PowerShell):
```
git clone https://github.com/CaDiBob/download_url.git
cd download_url
```

[uv](https://docs.astral.sh/uv/#installation) должен быть установлен

```
uv sync
```

### Аргументы

Скрипт принимает аргументы.

Обязательный:
```
--url=ссылку на контент или страницу
```
Необязательные:
```
--count=количество запросов на загрузку контента, по умолчанию 10
--timeout=таймаут соединения, по умолчанию 10 секунд
```

### Запуск

```
uv run main.py --url=https://fonwall.ru/wallpaper/nature-insects-bee/ --timeout=1 --count=3
```

При успешном выполнении в консоль выводится:
```
Start download content.
Download speed - 0.23225 Mbit/s
```

Ссылки с параметрами нужно брать в кавычки: оболочка по-своему
обрабатывает символы `&`, `?` и некоторые другие.

```
uv run main.py --url="https://image.fonwall.ru/o/xc/warhammer-40000-power-armor-the-horned-helmet.jpeg?auto=compress&fit=resize&w=1200&h=670&display=large&domain=img3.fonwall.ru"
```

### Единицы измерения

Скорость выводится в мегабитах в секунду (Mbit/s), 1 Mbit = 1 000 000 бит.

Скорость = общий объём скачанных данных / суммарное время всех запросов.

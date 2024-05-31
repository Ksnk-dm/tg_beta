import os
import sys
import asyncio
from aiohttp import web

# Добавляем путь к директории с вашим приложением
sys.path.insert(0, os.path.dirname(__file__))

# Импортируем ваш основной файл
import main as app

# Создаем экземпляр web.Application
async def init():
    await app.main()

# Функция для старта приложения
async def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Bot is running!"]

# Создаем aiohttp-сервер и запускаем его
asyncio.run(init())
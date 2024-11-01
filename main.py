import aiohttp
import asyncio

async def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Пример API для получения данных
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()  # Парсим ответ в формате JSON
            print(data)

# Запускаем асинхронную функцию
asyncio.run(fetch_data())

from aiohttp import web

async def greet_user(request):
    name = request.match_info.get('name', "Anonymous")  # Получаем параметр маршрута
    return web.Response(text=f"Hello, {name}!")

app = web.Application()
app.add_routes([web.get('/greet/{name}', greet_user)])  # Маршрут с параметром

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)

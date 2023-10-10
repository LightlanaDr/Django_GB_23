from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

headers = {'Cache-Control': 'no-cache, must-revalidate'}


def main(request):
    body = """
    <title>Главная страница</title>
    <body>
        <div align="center">
            <h1>Главная страница</h1>
            <a href="http://127.0.0.1:8000/sem1/about/"><p>Страница обо мне</p></a>
        </div>
        <footer>
            <div align="center">
            <p> Swetlana Druzchkova * 2023</p>
            </div>
        </footer>
    </body>
    """
    logger.info(f'Главная страница открыта')
    return HttpResponse(body, charset='utf-8', headers=headers)


def about(request):
    body = """
    <title>Главная страница</title>
    <body>
        <div align="center">
            <h1>Страница обо мне</h1>
            <p>Светлана Дружкова, 30 лет</p>
            <p>Проживаю в г. Фрязино, МО</p>
            <a href="http://127.0.0.1:8000/sem1/main/"><p>Перейти на главную</p></a>
        </div>
        <footer>
            <div align="center">
            <p> Swetlana Druzchkova * 2023</p>
            </div>
        </footer>
    </body>
    """
    logger.info(f'Страница "О нас" открыта')
    return HttpResponse(body, charset='utf-8', headers=headers)
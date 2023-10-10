from django.http import HttpResponse
import logging
import random

logger = logging.getLogger(__name__)


def one(request):
    answer = ['Орёл', 'Решка']
    i = random.randint(0, 2)
    return HttpResponse(f'{answer[i]}')


def two(request):
    answer = random.randint(1, 7)
    return HttpResponse(f'{answer}')


def three(request):
    answer = random.randint(1, 100)
    return HttpResponse(f'{answer}')

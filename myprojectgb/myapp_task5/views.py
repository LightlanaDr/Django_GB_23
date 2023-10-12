from django.http import HttpResponse
import logging
import random

from django.shortcuts import render

logger = logging.getLogger(__name__)


def one(request, n):
    context = {'res': []}
    # n = int(request.GET.get('n', '5'))
    while n > 0:
        context['res'].append(random.choice(['Орёл', 'Решка']))
        n -= 1
    return render(request, "one.html", context)


def two(request):
    answer = random.randint(1, 7)
    return HttpResponse(f'{answer}')


def three(request):
    answer = random.randint(1, 100)
    return HttpResponse(f'{answer}')

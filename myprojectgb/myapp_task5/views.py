from django.http import HttpResponse
import logging
import random
from .forms import Form_of_choice

from django.shortcuts import render

logger = logging.getLogger(__name__)


def one(request, n):
    context = {'res': []}
    # n = int(request.GET.get('n', '5'))
    while n > 0:
        context['res'].append(random.choice(['Орёл', 'Решка']))
        n -= 1
    return render(request, "one.html", context)


def two(request, count):
    answer = random.randint(1, 7)
    return HttpResponse(f'{answer}')


def three(request):
    answer = random.randint(1, 100)
    return HttpResponse(f'{answer}')


def user_form(request):
    if request.method == 'POST':
        form = Form_of_choice(request.POST)
        if form.is_valid():
            choice = form.data['choice']
            count = int(form.data['count'])
            if choice == 'ОиЗ':
                return one(request, count)
            elif choice == 'Ки':
                return two(request, count)
            else:
                return three(request)
    else:
        form = Form_of_choice()
    return render(request, 'user_form.html', {'form': form})

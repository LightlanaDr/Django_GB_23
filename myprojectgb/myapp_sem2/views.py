from django.http import HttpResponse
import logging
import random
from .models import HeadsTails

logger = logging.getLogger(__name__)


def one(request):
    # logger.info(f'{request} request received')
    n = request.GET.get('n', '5')
    res = random.choice(['Orel', 'Reschka'])
    res_w = HeadsTails(res=res)
    res_w.save()
    data = HeadsTails.staticstic(n)
    return HttpResponse(data.items())

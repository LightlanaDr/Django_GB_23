from django.db import models
from django.utils import timezone


class HeadsTails(models.Model):
    rest_time = models.DateTimeField(default=timezone.now)
    res = models.CharField(max_length=50)

    @staticmethod
    def staticstic(n):
        n = int(n)
        dict_res = {'Orel': 0, 'Reschka': 0}
        query = list(HeadsTails.objects.all())
        list_res = query[-n:]
        for item in list_res:
            if 'Orel' in str(item):
                dict_res['Orel'] += 1
            elif 'Reschka' in str(item):
                dict_res['Reschka'] += 1
        return dict_res

    def __str__(self):
        return f"time:{self.rest_time}, res:{self.res}"

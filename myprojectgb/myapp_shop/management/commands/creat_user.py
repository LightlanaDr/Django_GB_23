from django.core.management import BaseCommand
from ...models import User


class Command(BaseCommand):
    help = "Generate fake user"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1, count + 1):
            user = User(name=f'Name{i}', email=f'mail{i}@mail.ru',
                            phone_number=f'+7926324387{i}', address=f'Moscow, d{i}')
            user.save()


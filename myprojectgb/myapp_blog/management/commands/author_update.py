from django.core.management.base import BaseCommand
from ...models import Author, Post


class Command(BaseCommand):
    help = "fide author id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
        parser.add_argument('email', type=str, help='Author email')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = Author.objects.filter(pk=pk).first()
        author.email = kwargs.get('email')
        author.save()
        self.stdout.write(f'author: {author}')





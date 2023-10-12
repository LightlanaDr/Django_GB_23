from django.core.management.base import BaseCommand
from ...models import Author, Post


class Command(BaseCommand):
    help = "fide author id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')


    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = Author.objects.filter(pk=pk).first()
        author.delete()
        self.stdout.write(f'author: {author}')





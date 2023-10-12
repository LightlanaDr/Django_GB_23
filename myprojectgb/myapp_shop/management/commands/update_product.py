from django.core.management import BaseCommand
from ...models import Product
class Command(BaseCommand):
    help = "find product id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('price', type=str, help='Price email')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        product.price = kwargs.get('price')
        product.save()
        self.stdout.write(f'product: {product}')




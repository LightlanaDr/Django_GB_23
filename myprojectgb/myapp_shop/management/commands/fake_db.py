import random

from django.core.management import BaseCommand
from ...models import User, Product, Order


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        products = ['milk', 'bread', 'meat', 'water', 'milk', 'bread', 'meat', 'water']

        total_price = 0

        for i in range(1, count + 1):
            user = User(name=f'Name{i}', email=f'mail{i}@mail.ru',
                        phone_number=f'+7926324387{i}', address=f'Moscow, d{i}')
            user.save()

            product = Product(name=f'{random.choice(products)}',
                              description=f'description', price=f'{random.randint(1, 1000)}',
                              count=f'{random.randint(1, 10)}')
            product.save()

        for j in range(1, count + 1):
            count_prod = random.randint(1, len(products))
            basket = []
            for i in range(1, count_prod):
                basket.append(random.randint(1, len(products)))
            user_rnd = random.randint(1, count - 1)
            user = User.objects.filter(pk=user_rnd).first()
            order = Order(customer=user)
            order.order_sum = total_price
            order.save()
            for item in basket:
                product = Product.objects.filter(pk=item).first()
                total_price += product.price
                order.products.add(product)

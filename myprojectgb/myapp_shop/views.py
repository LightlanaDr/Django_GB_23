from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404, render

from .models import User, Order


def user_orders(request, user_id):
    customer = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=customer).all()
    products = []

    for order in orders:
        products.append(str(order.products.all()).replace('<QuerySet [<', '')
                        .replace("Product: ", "")
                        .replace('>]>', '').split('>, <'))
    products.reverse()

    return render(request, 'myapp_shop/user_orders.html',
                  {'customer': customer, 'orders': orders, 'products': products})


def sorted_basket(request, user_id, days_ago):
    customer = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=customer).all()
    product_set = []
    today = datetime.now()
    before = today - timedelta(days=days_ago)
    for order in orders:
        if order.order_date < datetime.date(before):
            products = order.products.all()
            for product in products:
                if product not in product_set:
                    product_set.append(product)
        else:
            return render(request, 'myapp_shop/not_orders.html')
    return render(request, 'myapp_shop/user_products_all.html',
                  {'customer': customer, 'product_set': product_set, 'days_ago': days_ago})

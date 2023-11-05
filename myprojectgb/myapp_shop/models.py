from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    date_reg = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.name}, {self.email}, {self.phone_number}'


# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     count = models.IntegerField()
#     publication = models.DateField(auto_now_add=True)
#     image = models.ImageField(verbose_name='Фото', upload_to='products/')
#
#
#
#     def __str__(self):
#         return (f'Product: {self.name}: {self.description}, '
#                 f'price: {self.price}, count: {self.count}')

class ProductNew(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    publication = models.DateField(auto_now_add=True)
    image = models.ImageField(verbose_name='Фото', upload_to='products/')

    def __str__(self):
        return (f'Product: {self.name}: {self.description}, '
                f'price: {self.price}, count: {self.count}')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductNew)
    order_sum = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Order: {self.customer.name}, '
                f'sum total {self.order_sum} date {self.order_date}')



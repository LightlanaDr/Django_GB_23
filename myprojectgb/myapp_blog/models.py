
# Create your models here.
from django.db import models


class Author(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField(default='2023-6-20')

    def __str__(self):
        return f'Name: {self.f_name}{self.l_name}, email: {self.email}'


# заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи с удалением связанных объектов при удалении автора
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья со значением по умолчанию
# False

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, default='category')
    show_content = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'Title is {self.title}'

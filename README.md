## Урок 1. Введение в Django
### Создайте пару представлений в вашем первом [приложении](https://github.com/LightlanaDr/Django_GB_23/tree/7776098ee717d5f53b3b66f3811c2344dc2d3630/myprojectgb/myapp_sem1):
— [главная](https://github.com/LightlanaDr/Django_GB_23/blob/7776098ee717d5f53b3b66f3811c2344dc2d3630/myprojectgb/myapp_sem1/views.py)
— [о себе](https://github.com/LightlanaDr/Django_GB_23/blob/7776098ee717d5f53b3b66f3811c2344dc2d3630/myprojectgb/myapp_sem1/views.py).

Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.

Сохраняйте в логи данные о посещении страниц.

## Урок 2. Работа с моделями
 [Поля модели "Заказ":](https://github.com/LightlanaDr/Django_GB_23/blob/master/myprojectgb/myapp_shop/models.py)
○ связь с моделью "Клиент", указывает на клиента,
сделавшего заказ
○ связь с моделью "Товар", указывает на товары,
входящие в заказ
○ общая сумма заказа
○ дата оформления заказа
### *Допишите несколько функций [CRUD](https://github.com/LightlanaDr/Django_GB_23/tree/master/myprojectgb/myapp_shop/management) для работы с
моделями по желанию. Что по вашему мнению актуально в
такой базе данных.
 

## Урок 3. Работа с представлениями и шаблонами
### Задание
Продолжаем работать с товарами и заказами.

Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
— за последние 7 дней (неделю)
— за последние 30 дней (месяц)
— за последние 365 дней (год)

Товары в списке не должны повторятся.
[views.py](https://github.com/LightlanaDr/Django_GB_23/blob/master/myprojectgb/myapp_shop/views.py)
[templates](https://github.com/LightlanaDr/Django_GB_23/tree/master/myprojectgb/myapp_shop/templates/myapp_shop)

## Урок 4. Работа с формами
### Задание
Доработаем задачу про клиентов, заказы и товары из
прошлого семинара.
Создайте [форму для редактирования товаров в базе](https://github.com/LightlanaDr/Django_GB_23/blob/master/myprojectgb/myapp_shop/forms.py)
данных.
Домашнее задание
Измените модель продукта, добавьте поле для хранения
фотографии продукта.
[Создайте форму, которая позволит сохранять фото.](https://github.com/LightlanaDr/Django_GB_23/blob/master/myprojectgb/myapp_shop/forms.py)

## Урок 5. Работа с административной панелью
### Задание
Настройте под свои нужды вывод информации о [клиентах, товарах и заказах](https://github.com/LightlanaDr/Django_GB_23/blob/master/myprojectgb/myapp_shop/admin.py) 
на страницах вывода информации об объекте и вывода списка объектов.



# Generated by Django 4.2.6 on 2023-11-05 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_shop', '0006_alter_product_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

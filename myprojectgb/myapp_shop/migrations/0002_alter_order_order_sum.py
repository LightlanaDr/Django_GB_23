# Generated by Django 4.2.6 on 2023-10-19 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_sum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]

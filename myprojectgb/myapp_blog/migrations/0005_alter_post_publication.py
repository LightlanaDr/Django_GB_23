# Generated by Django 4.2.6 on 2023-11-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication',
            field=models.DateField(),
        ),
    ]

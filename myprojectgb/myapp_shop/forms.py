from django import forms

from .models import ProductNew


class ProductCreate(forms.ModelForm):
    class Meta:
        model = ProductNew
        fields = ['name', 'description', 'price', 'count', 'image']
        labels = {'name': 'Имя', 'description': 'Описание',
                  'price': 'Стоимость', 'count': 'Количество', 'image': 'Фото',
                 }

        widgets = {
            'image': forms.FileInput(),
        }

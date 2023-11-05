from django import forms


class Form_of_choice(forms.Form):
    choice = forms.ChoiceField(choices=[('ОиЗ', 'Орел и Решка'), ('К', 'Кости'), ('Ч', 'Число')])
    count = forms.IntegerField(min_value=1, max_value=64,
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))

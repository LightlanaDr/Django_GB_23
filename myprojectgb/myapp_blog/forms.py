import datetime
from django import forms

from .models import Author, Post


class AuthorForm(forms.Form):
    f_name = forms.CharField(max_length=20, widget=forms.TimeInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    l_name = forms.CharField(max_length=100, widget=forms.TimeInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите фамилию пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@mail.ru'}))
    biography = forms.CharField(max_length=20, widget=forms.TimeInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите биографию пользователя'}))
    birthday = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control'}))


class NewPost(forms.ModelForm):
    # choices = [(i.id, i.get_fullname()) for i in Author.objects.all()] --- Первый вариант
    # author = forms.ChoiceField(choices=choices) ---- Первый вариант вывода информации из бд

    # name = forms.CharField()
    # text = forms.CharField(widget=forms.Textarea(attrs={'size': 1000}))
    # author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label='Выбрать автора')
    # Второй вариант вывода инфы из бд

    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'publication']
        labels = {'author': 'Автор', 'title': '',
                  'content': '', 'publication': ''}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input_text long_input',
                                            'placeholder': 'Название статьи: '}),
            'author': forms.Select(attrs={'class': 'input_text long_input'}),
            'content': forms.Textarea(attrs={'class': 'input_text long_input',
                                             'cols': 100, 'rows': 10,
                                             'placeholder': 'Содержание статьи: ',
                                             }),
            'publication': forms.DateInput(attrs={'class': 'input_text long_input',
                                                  'type': 'date'}),
        }


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=20,
                              widget=forms.Textarea(attrs={'class': 'form-control'}))
    post = forms.ModelChoiceField(label='Post  ', empty_label='please select',
                                  queryset=Post.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}))

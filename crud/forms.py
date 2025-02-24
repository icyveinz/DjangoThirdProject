from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', help_text='Введите свое имя', min_length=2, max_length=10)
    age = forms.IntegerField(min_value=1, max_value=100)
    weight = forms.DecimalField(min_value=3, max_value=200, decimal_places=2)
    reklama = forms.BooleanField(label='Coглacны получать рекламу?', required=False)
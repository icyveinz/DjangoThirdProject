from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Ваше имя")
    age = forms.IntegerField(label="Ваш возраст")
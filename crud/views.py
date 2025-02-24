from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
from .models import Person


def index(request):
    people = Person.objects.all()
    userform = UserForm(request.POST)
    return render(request, 'index.html', {'users': people, 'form': userform})

def create_user(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']  # получить значение поля Имя
            age = userform.cleaned_data['age']  # получить значение поля Возраст
            person = Person(name=name, age=age)
            person.save()
        return HttpResponseRedirect('/')
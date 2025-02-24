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

def edit_user_page(request, user_id):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            person = Person.objects.get(id=user_id)
            person.name = userform.cleaned_data['name']
            person.age = userform.cleaned_data['age']
            person.save()
        return HttpResponseRedirect('/')

def edit_user(request, user_id):
    userform = UserForm(request.POST)
    return render(request, 'edit_user.html', {'form': userform, 'action_url' : '/'})
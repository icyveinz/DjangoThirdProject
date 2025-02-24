from django.shortcuts import render
from .forms import UserForm


def index(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']  # получить значение поля Имя
            age = userform.cleaned_data['age']  # получить значение поля Возраст
            return render(
                request,
                'reply.html',
                {"content": {"name": name, "age": age}})
        else:
            return render(
                request,
                'reply.html',
                {"content": {"name": "You haven't passed the validation", "age": ""}})
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})
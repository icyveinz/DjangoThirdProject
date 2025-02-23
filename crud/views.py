from django.shortcuts import render
from crud.forms import UserForm


# Create your views here.

def index(request):
    userform = UserForm()
    return render(request, 'index.html', {'form': userform})
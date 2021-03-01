from django.shortcuts import render, redirect, get_object_or_404
from utilisateur.forms import UserForm
from utilisateur.models import User

from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, login, logout



def connection(request):

    return render(request, 'connection.html', locals())
    #return redirect('feed')

def create_user(request, id_user=None):
    #a modif (basé sur ticket, créé ET modif)
    User = get_user_model()
    if request.method == "GET":
        form = UserForm()
        return render(request, 'register.html', locals())
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connection')

def test(request):
    users = User.objects.all()
    return render(request, 'test.html', {'users': users})

def disconnect(request):
    pass

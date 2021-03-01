from django.shortcuts import render, redirect, get_object_or_404
from utilisateur.forms import UserForm
from utilisateur.models import User

from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, login, logout


def connection(request, id_user=None):
    
    """instance_user = User.objects.get(pk=id_user) if id_user is not None else None
    if request.method == "POST":
        form = UserForm(request.POST, instance=instance_user)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if form.is_valid():
            return redirect('connection')
        #if user is not None:
        #    login(request, user)
        #    return redirect('test.html')
    return render(request, 'connection.html')"""

    '''instance_user = User.objects.get(pk=id_user) if id_user is not None else None
    if request.method == "GET":
        form = UserForm(instance=instance_user)
        return render(request, 'connection.html', locals())

    elif request.method == "POST":
        form = UserForm(request.POST, instance=instance_user)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('test')'''
    return redirect('test')


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


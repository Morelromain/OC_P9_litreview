from django.shortcuts import render, redirect, get_object_or_404
from utilisateur.forms import UserForm
from utilisateur.models import User
from utilisateur.models import UserFollows
from django.contrib.auth.decorators import login_required

from utilisateur.forms import UserFollowsForm


from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, login, logout



def connection(request):

    return render(request, 'connection.html', locals())
    #return redirect('feed')

def create_user(request, id_user=None):

    User = get_user_model()
    if request.method == "GET":
        form = UserForm()
        return render(request, 'register.html', locals())
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            modif_form = form.save(commit=False)
            if modif_form.password == modif_form.first_name:
                modif_form.set_password(modif_form.password)
                modif_form.first_name = ""
                modif_form.save()
                return redirect('connection')
            return render(request, 'register.html', locals())


@login_required
def subscription(request):
    usersfollows = UserFollows.objects.filter(user = request.user)
    followeds = UserFollows.objects.filter(followed_user = request.user)

    if request.method == "GET":
        form = UserFollowsForm()
        return render(request, 'subscription.html', locals())
    elif request.method == "POST":
        form = UserFollowsForm(request.POST) 
        if form.is_valid():
            modif_form = form.save(commit=False)
            modif_form.user = request.user
            #aaa = get_object_or_404(UserFollows, pk=modif_form.followed_user)
            #modif_form.followed_user = aaa.id
            if modif_form.followed_user == request.user:
                pass #erreur
            else:
                try:
                    modif_form.save()
                except:
                    pass #erreur
            return redirect('subscription')

@login_required
def delete_subs(request, id_subs):
    subs = get_object_or_404(UserFollows, pk=id_subs)
    subs.delete()
    return redirect('subscription')

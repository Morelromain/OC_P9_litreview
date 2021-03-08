from django.shortcuts import render, redirect, get_object_or_404
from utilisateur.forms import UserForm
from utilisateur.models import User
from utilisateur.models import UserFollows
from django.contrib.auth.decorators import login_required

from utilisateur.forms import UserFollowsForm


from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, login, logout



def connection(request):
    pass
    #return render(request, 'connection.html', locals())
    #return redirect('settings.LOGIN_URL')

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
            else:
                erreur = "Les mots de passes saisis ne sont pas identique"
        else:
            erreur = "Nom déjà pris"
        return render(request, 'register.html', locals())


@login_required
def subscription(request):
    usersfollows = UserFollows.objects.filter(user = request.user)
    followeds = UserFollows.objects.filter(followed_user = request.user)

    if request.method == "GET":
        #formu = UserForm()
        form = UserFollowsForm()
        return render(request, 'subscription.html', locals())
    elif request.method == "POST":
        form = UserFollowsForm(request.POST) 
        #formu = UserForm(request.POST)

        if form.is_valid():
            modif_form = form.save(commit=False)
            modif_form.user = request.user
            #modif_form.followed_user = request.user
            try : 
                test2 = User.objects.get(username = modif_form.confirm)
            except :
                erreur = "Cette personne n'existe pas"
                return render(request, 'subscription.html', locals())
            modif_form.followed_user = test2
            modif_form.confirm = ""
            if modif_form.followed_user == request.user:
                erreur = "Vous ne pouvez vous suivre vous même"
            else:
                try:
                    modif_form.save()
                except:
                    erreur = "Vous suivez déjà cette personne"
            return render(request, 'subscription.html', locals())

@login_required
def delete_subs(request, id_subs):
    subs = get_object_or_404(UserFollows, pk=id_subs)
    subs.delete()
    return redirect('subscription')

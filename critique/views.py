from django.shortcuts import render, redirect, get_object_or_404

from critique.forms import ReviewForm
from critique.forms import TicketForm

from critique.models import Review
from critique.models import Ticket
from utilisateur.models import UserFollows

from itertools import chain
from django.db.models import CharField, Value
#from django.template.context_processors import csrf


"""def get_users_viewable_reviews(request_user):
    usersfollows = UserFollows.objects.filter(user = request_user)
    reviews2 = Review.objects.filter(user = usersfollows.user)
    return reviews2"""

def feed(request):
    """reviews = Review.objects.all()  
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = Ticket.objects.all() 
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))"""

    usersfollows = UserFollows.objects.filter(user = request.user)

    reviews = Review.objects.filter(user = request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    for uf in usersfollows:
        reviews2 = Review.objects.filter(user = uf.followed_user)
        reviews2 = reviews2.annotate(content_type=Value('REVIEW', CharField()))
        reviews = sorted(chain(reviews, reviews2), key=lambda post: post.time_created)
    
    tickets = Ticket.objects.filter(user = request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    for uf in usersfollows:
        tickets2 = Ticket.objects.filter(user = uf.followed_user)
        tickets2 = tickets2.annotate(content_type=Value('TICKET', CharField()))
        tickets = sorted(chain(tickets, tickets2), key=lambda post: post.time_created)
    
    posts = sorted(
        chain(reviews, tickets), 
        key=lambda post: post.time_created, 
        reverse=True
    )
    return render(request, 'feed.html', locals())


def create_ticket(request, id_ticket=None):
    instance_ticket = Ticket.objects.get(pk=id_ticket) if id_ticket is not None else None
    if request.method == "GET":
        form = TicketForm(instance=instance_ticket)
        return render(request, 'addticket.html', locals())
    elif request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=instance_ticket)
        if form.is_valid():
            modif_form = form.save(commit=False)
            modif_form.user = request.user
            #modif_form.response = True
            modif_form.save()
            return redirect('feed')


def create_review(request, id_review=None): #Modif review
    instance_review = Review.objects.get(pk=id_review) if id_review is not None else None
    instance_ticket = Ticket.objects.get(pk=instance_review.ticket.id)
    if request.method == "GET":
        form = ReviewForm(instance=instance_review)
        return render(request, 'addreview.html', locals())
    elif request.method == "POST":
        form = ReviewForm(request.POST, instance=instance_review)
        if form.is_valid():
            aga = form.save(commit=False)
            aga.save()
            #Ticket.response = True
            #formt.save()
            return redirect('feed')


def create_t_and_r(request, id_ticket=None):
    if request.method == "GET":
        t_form = TicketForm()
        r_form = ReviewForm()
        return render(request, 'addtandr.html', locals())

    elif request.method == "POST":
        t_form = TicketForm(request.POST, request.FILES)
        r_form = ReviewForm(request.POST)
        if t_form.is_valid and r_form.is_valid():

            t_modif = t_form.save(False)
            t_modif.user = request.user
            t_modif.response = True
            t_modif.save()

            review_f = r_form.save(False)
            review_f.ticket = t_modif
            review_f.user = request.user
            review_f.save()

            return redirect('feed')


def link_review(request, id_ticket=None): 
    instance_ticket = Ticket.objects.get(pk=id_ticket) if id_ticket is not None else None
    if request.method == "GET":
        form = ReviewForm()
        return render(request, 'linkreview.html', locals())
    elif request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            modif_form = form.save(commit=False)
            modif_form.ticket = instance_ticket
            modif_form.user = request.user
            modif_form.save()
            instance_ticket.response = True
            instance_ticket.save()
            return redirect('feed')


def view_review(request, id_review):
    review = get_object_or_404(Review, pk=id_review)
    ticket = get_object_or_404(Ticket, pk=review.ticket.id)
    return render(request, 'view_review.html', locals())


def view_ticket(request, id_ticket):
    ticket = get_object_or_404(Ticket, pk=id_ticket)
    return render(request, 'view_ticket.html', locals())

def delete_review(request, id_review):
    review = get_object_or_404(Review, pk=id_review)
    review.delete()
    return redirect('myposts')

def delete_ticket(request, id_ticket):
    ticket = get_object_or_404(Ticket, pk=id_ticket)
    ticket.delete()
    return redirect('myposts')

def view_myposts(request):

    tickets = Ticket.objects.filter(user = request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    reviews = Review.objects.filter(user = request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    for tick in tickets:
        reviews2 = Review.objects.filter(ticket = tick.id)
        reviews2 = reviews2.annotate(content_type=Value('REVIEW', CharField()))
        reviews = sorted(chain(reviews, reviews2), key=lambda post: post.time_created)


    

    posts = sorted(
        chain(reviews, tickets), 
        key=lambda post: post.time_created, 
        reverse=True
    )
    return render(request, 'myposts.html', locals())




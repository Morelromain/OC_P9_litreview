from django.shortcuts import render, redirect, get_object_or_404

from critique.forms import ReviewForm
from critique.forms import TicketForm

from critique.models import Review
from critique.models import Ticket

from itertools import chain
from django.db.models import CharField, Value
#from django.template.context_processors import csrf


def feed(request):
    reviews = Review.objects.all()  
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = Ticket.objects.all() 
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    posts = sorted(
        chain(reviews, tickets), 
        key=lambda post: post.time_created, 
        reverse=True
    )
    return render(request, 'feed.html', context={'posts': posts})


def create_ticket(request, id_ticket=None):
    instance_ticket = Ticket.objects.get(pk=id_ticket) if id_ticket is not None else None
    if request.method == "GET":
        form = TicketForm(instance=instance_ticket)
        return render(request, 'addticket.html', locals())
    elif request.method == "POST":
        form = TicketForm(request.POST, instance=instance_ticket)
        if form.is_valid():
            modif_form = form.save(commit=False)
            modif_form.user = request.user
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
            return redirect('feed')


def create_t_and_r(request, id_ticket=None):
    if request.method == "GET":
        t_form = TicketForm()
        r_form = ReviewForm()
        #args = {}
        #args.update(csrf(request))
        #args['t_form'] = t_form
        #args['r_form'] = r_form
        return render(request, 'addtandr.html', locals())

    elif request.method == "POST":
        t_form = TicketForm(request.POST)
        r_form = ReviewForm(request.POST)
        if t_form.is_valid and r_form.is_valid():

            t_modif = t_form.save(False)
            t_modif.save()

            review_f = r_form.save(False)
            review_f.ticket = t_modif
            review_f.user = request.user
            review_f.save()

            return redirect('feed')
            #return render(request, 'linkreview.html',)


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
            return redirect('feed')


def view_review(request, id_review):
    review = get_object_or_404(Review, pk=id_review)
    return render(request, 'view_review.html', locals())


def view_ticket(request, id_ticket):
    ticket = get_object_or_404(Ticket, pk=id_ticket)
    return render(request, 'view_ticket.html', locals())

def delete_review(request, id_review):
    review = get_object_or_404(Review, pk=id_review)
    review.delete()
    return redirect('feed')

def delete_ticket(request, id_ticket):
    ticket = get_object_or_404(Ticket, pk=id_ticket)
    ticket.delete()
    return redirect('feed')


from django.http import HttpResponse


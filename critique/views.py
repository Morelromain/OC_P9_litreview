from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value

from critique.forms import ReviewForm
from critique.forms import TicketForm
from critique.models import Review
from critique.models import Ticket
from utilisateur.models import UserFollows


@login_required
def create_ticket(request, id_ticket=None):
    """create or edit a request for review"""
    instance_ticket = Ticket.objects.get(pk=id_ticket) if id_ticket is not None else None
    if request.method == "GET":
        form = TicketForm(instance=instance_ticket)
        return render(request, 'addticket.html', locals())
    elif request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=instance_ticket)
        if form.is_valid():
            modif_form = form.save(commit=False)
            modif_form.user = request.user
            modif_form.save()
            return redirect('feed')


@login_required
def create_review(request, id_review=None):
    """edit a review"""
    instance_review = Review.objects.get(pk=id_review) if id_review is not None else None
    instance_ticket = Ticket.objects.get(pk=instance_review.ticket.id)
    if request.method == "GET":
        form = ReviewForm(instance=instance_review)
        return render(request, 'addreview.html', locals())
    elif request.method == "POST":
        form = ReviewForm(request.POST, instance=instance_review)
        if form.is_valid():
            modif_form = form.save(commit=False)
            modif_form.rating = request.POST.get('tabs')
            modif_form.save()
            return redirect('feed')


@login_required
def create_t_and_r(request):
    """create a request for review and a review"""
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
            t_modif.save()
            review_f = r_form.save(False)
            review_f.ticket = t_modif
            review_f.user = request.user
            review_f.rating = request.POST.get('tabs')
            review_f.save()
            return redirect('feed')


@login_required
def link_review(request, id_ticket):
    """create a review linked to a request"""
    instance_ticket = Ticket.objects.get(pk=id_ticket)
    if request.method == "GET":
        form = ReviewForm()
        return render(request, 'linkreview.html', locals())
    elif request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            modif_form = form.save(commit=False)
            modif_form.ticket = instance_ticket
            modif_form.user = request.user
            modif_form.rating = request.POST.get('tabs')
            modif_form.save()
            instance_ticket.save()
            return redirect('feed')


@login_required
def delete_review(request, id_review):
    """remove a review"""
    review = get_object_or_404(Review, pk=id_review)
    review.delete()
    return redirect('myposts')


@login_required
def delete_ticket(request, id_ticket):
    """remove a request for review and its reviesws"""
    ticket = get_object_or_404(Ticket, pk=id_ticket)
    ticket.delete()
    return redirect('myposts')


@login_required
def feed(request):
    """display their posts and replies and those of its subscribers"""
    usersfollows = UserFollows.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)
    tickets = Ticket.objects.filter(user=request.user)
    ticket_made = []
    for revi in reviews:
        ticket_made.append(revi.ticket)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    for tick in tickets:
        reviews3 = Review.objects.filter(ticket=tick.id).exclude(user=request.user)
        reviews3 = reviews3.annotate(content_type=Value('REVIEW', CharField()))
        reviews = sorted(chain(reviews, reviews3), key=lambda post: post.time_created)
    for uf in usersfollows:
        reviews2 = Review.objects.filter(user=uf.followed_user)
        reviews2 = reviews2.annotate(content_type=Value('REVIEW', CharField()))
        reviews = sorted(chain(reviews, reviews2), key=lambda post: post.time_created)
    reviews = set(reviews)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    for uf in usersfollows:
        tickets2 = Ticket.objects.filter(user=uf.followed_user)
        tickets2 = tickets2.annotate(content_type=Value('TICKET', CharField()))
        tickets = sorted(chain(tickets, tickets2), key=lambda post: post.time_created)
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    return render(request, 'feed.html', locals())


@login_required
def view_myposts(request):
    """display their posts"""
    tickets = Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    return render(request, 'myposts.html', locals())

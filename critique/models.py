from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class Ticket(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=2048, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="")
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Ticket: ' + self.title


class Review(models.Model):
    objects = models.Manager()
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Review: ' + self.headline

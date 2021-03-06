from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass


class UserFollows(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following_by')
    confirm = models.CharField(max_length=128, blank=True)

    class Meta:
        unique_together = ('user', 'followed_user', )
    def __str__(self):
        return 'Suivis: ' + str(self.user) + " > " + str(self.followed_user)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserFollows


class UserFollowsAdmin(admin.ModelAdmin):
    exclude = ('confirm',)

admin.site.register(User, UserAdmin)
admin.site.register(UserFollows, UserFollowsAdmin)

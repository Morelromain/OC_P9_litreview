from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserFollows




#admin.site.register(User)
admin.site.register(User, UserAdmin)



class UserFollowsAdmin(admin.ModelAdmin):
    exclude = ('confirm',)

admin.site.register(UserFollows, UserFollowsAdmin)




from django.contrib import admin

from app_facebook.models import User, UserScore,Settings

admin.site.register(User)
admin.site.register(UserScore)
admin.site.register(Settings)
# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import App, User

admin.site.register(User, UserAdmin)


class AppAdmin(admin.ModelAdmin):
    list_display = ("url", "created_at", "enabled")


admin.site.register(App, AppAdmin)

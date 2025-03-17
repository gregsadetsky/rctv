from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import App, User

admin.site.register(User, UserAdmin)


class AppAdmin(admin.ModelAdmin):
    list_display = ("url", "created_at", "enabled")
    actions = ["disable_apps", "enable_apps"]

    def disable_apps(self, request, queryset):
        updated = queryset.update(enabled=False)
        self.message_user(
            request,
            f"{updated} {'app was' if updated == 1 else 'apps were'} successfully disabled.",
        )

    disable_apps.short_description = "Disable selected apps"

    def enable_apps(self, request, queryset):
        updated = queryset.update(enabled=True)
        self.message_user(
            request,
            f"{updated} {'app was' if updated == 1 else 'apps were'} successfully enabled.",
        )

    enable_apps.short_description = "Enable selected apps"


admin.site.register(App, AppAdmin)

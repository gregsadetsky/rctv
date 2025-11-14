from django.urls import include, path
import django_eventstream

from core.views.developers.index import add_app, developers, edit_app
from core.views.index import index, get_all_apps_for_tauri
from core.views.oauth.oauth_redirect import oauth_redirect

urlpatterns = [
    path("", index, name="index"),
    path("get_all_apps_for_tauri", get_all_apps_for_tauri, name="get_all_apps_for_tauri"),
    path("developers", developers, name="developers"),
    path("developers/edit_app", edit_app, name="edit_app"),
    path("developers/add_app", add_app, name="add_app"),
    path("oauth_redirect", oauth_redirect, name="oauth_redirect"),
    path("events", include(django_eventstream.urls), {"channels": ["events"]}),
]

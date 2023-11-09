from django.urls import path

from core.views.api.events import events
from core.views.api.hub_visits import hub_visits_for_today
from core.views.api.user_is_authed import user_is_authed
from core.views.developers.index import add_app, developers, edit_app
from core.views.index import app, index
from core.views.oauth.oauth_redirect import oauth_redirect

urlpatterns = [
    path("", index, name="index"),
    path("app/<int:app_index>", app, name="app"),
    path("developers", developers, name="developers"),
    path("developers/edit_app", edit_app, name="edit_app"),
    path("developers/add_app", add_app, name="add_app"),
    path("oauth_redirect", oauth_redirect, name="oauth_redirect"),
    # api/userIsAuthed is the only un-authed api view,
    # since it returns to the sdk/client-side wheter the user is auth'ed.
    path("api/userIsAuthed", user_is_authed, name="user_is_authed"),
    path("api/hubVisitsForToday", hub_visits_for_today, name="hub_visits_for_today"),
    path("api/events", events, name="events"),
]

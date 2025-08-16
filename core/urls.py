from django.urls import path

from core.views.api.events import events
from core.views.api.hub_visits import hub_visits_for_today
from core.views.api.user_is_authed import user_is_authed
from core.views.api.zulip_stream_messages import zulip_stream_messages
from core.views.developers.index import add_app, developers, edit_app
from core.views.index import app, index, get_all_apps_for_tauri
from core.views.internal_api.unprocessed_zulip_message import (
    get_unprocessed_zulip_messages,
)
from core.views.oauth.oauth_redirect import oauth_redirect
from core.views.zulip.incoming_webhook import incoming_webhook

urlpatterns = [
    path("", index, name="index"),
    path("app/<int:app_index>", app, name="app"),
    path("get_all_apps_for_tauri", get_all_apps_for_tauri, name="get_all_apps_for_tauri"),
    path("developers", developers, name="developers"),
    path("developers/edit_app", edit_app, name="edit_app"),
    path("developers/add_app", add_app, name="add_app"),
    path("oauth_redirect", oauth_redirect, name="oauth_redirect"),
    # api/... are views used by the SDK to return data to tv apps
    # api/userIsAuthed is the only un-authed api view,
    # since it returns to the sdk/client-side wheter the user is auth'ed.
    path("api/userIsAuthed", user_is_authed, name="user_is_authed"),
    path("api/hubVisitsForToday", hub_visits_for_today, name="hub_visits_for_today"),
    path("api/events", events, name="events"),
    path(
        "api/zulipStreamMessages",
        zulip_stream_messages,
        name="zulip_stream_messages",
    ),
    path("zulip/incoming_webhook", incoming_webhook, name="incoming_webhook"),
    # api used by the tv to talk to us
    path(
        "internal-api/get_unprocessed_zulip_messages",
        get_unprocessed_zulip_messages,
        name="get_unprocessed_zulip_messages",
    ),
]

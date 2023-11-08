from django.urls import path

from core.views.api.events import events
from core.views.api.hub_visits import hub_visits
from core.views.index import app, index

urlpatterns = [
    path("", index, name="index"),
    path("app/<int:app_index>", app, name="app"),
    path("api/hubVisits", hub_visits, name="hub_visits"),
    path("api/events", events, name="events"),
]

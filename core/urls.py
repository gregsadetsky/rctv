from django.urls import path

from core.views.index import app, index

urlpatterns = [
    path("", index, name="index"),
    path("app/<int:app_index>", app, name="app"),
]

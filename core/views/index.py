from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from ..models import App
from ..utils.basicauth import basicauth


def index(request):
    return render(request, "core/index.html")


@basicauth
def app(request, app_index):
    all_apps = App.objects.filter(enabled=True)

    if len(all_apps) == 0:
        return HttpResponse(b"please come back another time")

    # sanity
    if app_index >= len(all_apps):
        app_index = 0

    app_object = all_apps[app_index]

    return render(
        request,
        "core/app.html",
        {
            "app_index": app_index,
            "next_app_index": (app_index + 1) % len(all_apps),
            "app": app_object,
            "meta_refresh_seconds": settings.APP_META_REFRESH_SECONDS,
        },
    )

from django.conf import settings
from django.shortcuts import render


def index(request):
    return render(request, "core/index.html")


def app(request, app_index):
    return render(
        request,
        "core/app.html",
        {
            "app_index": app_index,
            # FIXME
            "next_app_index": app_index,
            "meta_refresh_seconds": settings.APP_META_REFRESH_SECONDS,
        },
    )

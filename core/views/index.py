from django.conf import settings
from django.http import HttpResponse, JSONResponse
from django.shortcuts import render

from ..models import App
from ..utils.views_tv_token import view_or_expect_tv_token


# completely public view
def index(request):
    return render(request, "core/index.html")


# tv view, require basic auth (which maps to django users)
@view_or_expect_tv_token
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
        },
    )

@view_or_expect_tv_token
def get_all_apps_for_tauri(request):
    # return all enabled apps as json
    all_apps = App.objects.filter(enabled=True)
    apps_data = []
    for app in all_apps:
        apps_data.append(
            {
                "url": app.url,
            }
        )
    return JSONResponse({"apps": apps_data})

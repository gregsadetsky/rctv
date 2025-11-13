from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from ..models import App
from ..utils.views_tv_token import view_or_expect_tv_token


# completely public view
def index(request):
    return render(request, "core/index.html")


# tv api, require basic auth (which maps to django users)
@view_or_expect_tv_token
def get_all_apps_for_tauri(request):
    # return all enabled apps as json
    all_apps = App.objects.filter(enabled=True).order_by("created_at")
    apps_data = []
    for app in all_apps:
        apps_data.append(
            {
                "url": app.url,
                "on_screen_duration_seconds": app.on_screen_duration_seconds,
            }
        )
    return JsonResponse({"apps": apps_data})

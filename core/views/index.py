from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from ..models import App, ZulipImgRequest
from ..utils.views_basicauth import basicauth


# completely public view
def index(request):
    return render(request, "core/index.html")


# tv view, require basic auth (which maps to django users)
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


def get_next_zulip_image_to_show(request):
    oldest_not_processed_image = (
        ZulipImgRequest.objects.filter(processed=False).order_by("created_at").first()
    )
    if oldest_not_processed_image is None:
        return JsonResponse({"img_url": None})
    oldest_not_processed_image.processed = True
    oldest_not_processed_image.save()
    return JsonResponse({"img_url": oldest_not_processed_image.img_url})

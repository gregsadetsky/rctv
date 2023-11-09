from core.models import App
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from ...utils.views_auth import user_authentication_required
from ..oauth.utils import get_rc_oauth


# entry point for oauth login
# i.e. developers should go here to login with recurse oauth
def developers(request):
    if not request.user.is_authenticated:
        return get_rc_oauth().authorize_redirect(
            request, settings.RC_OAUTH_REDIRECT_URI
        )

    all_apps = App.objects.all()

    return render(request, "core/developers.html", {"all_apps": all_apps})


@user_authentication_required
@require_http_methods(["POST"])
def edit_app(request):
    action = request.POST.get("action")
    assert action in ["enable", "disable", "delete"]
    app_id = request.POST.get("app_id")
    app = get_object_or_404(App, id=app_id)

    if action == "enable":
        app.enabled = True
        app.save()
    elif action == "disable":
        app.enabled = False
        app.save()
    elif action == "delete":
        app.delete()
    else:
        raise Exception("Invalid action")

    return redirect(reverse("developers"))


@user_authentication_required
@require_http_methods(["POST"])
def add_app(request):
    app_url = request.POST.get("url")
    app_uses_api = request.POST.get("uses_api") == "on"

    errors = []
    if len(app_url.strip()) == 0:
        errors.append("Please enter a URL")
    if not app_url.startswith("http"):
        errors.append("Please enter a valid URL")

    if len(errors):
        return HttpResponse(
            ("<br/>".join(errors) + "<br/>go back and please try again").encode("utf-8")
        )

    app = App(
        url=app_url,
        uses_api=app_uses_api,
    )
    app.save()

    return redirect(reverse("developers"))

from core.models import App
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django_eventstream import send_event

from ...utils.views_auth import user_authentication_required
from ..oauth.utils import get_rc_oauth


# entry point for oauth login
# i.e. developers should go here to login with recurse oauth
# ALSO, this is the entry point for developers who just included
# the app-sdk.js script, and tried to make an RC API call that we provide.
# the app-sdk.js will ping /apiu/userIsAuthed to see if the user is authed,
# and if it's not the case, will redirect to /developers?redirect_uri=...
# with the app url as a param.
# - store the redirect as part of a session for this (anonymous to us) user
# - go through the oauth flow, and if/when we emerge on the other side of it
# in views.oauth_redirects, redirect to the redirect_uri (which is the app url)
def developers(request):
    if not request.user.is_authenticated:
        redirect_uri = request.GET.get("redirect_uri", None)
        if redirect_uri:
            request.session["redirect_uri"] = redirect_uri

        return get_rc_oauth().authorize_redirect(
            request, settings.RC_OAUTH_REDIRECT_URI
        )

    all_apps = list(App.objects.all())

    app_index = 0
    for app in all_apps:
        if app.enabled:
            app.app_index = app_index
            app_index += 1

    return render(request, "core/developers.html", {"all_apps": all_apps})


@user_authentication_required
@require_http_methods(["POST"])
def edit_app(request):
    action = request.POST.get("action")
    assert action in ["enable", "disable", "delete", "show_immediately"]
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
    elif action == "show_immediately":
        send_event("events", "show_immediately", {"url": app.url})
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

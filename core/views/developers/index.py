from core.models import App
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from ..oauth.utils import get_rc_oauth


def developers(request):
    if not request.user.is_authenticated:
        return get_rc_oauth().authorize_redirect(
            request, settings.RC_OAUTH_REDIRECT_URI
        )

    all_apps = App.objects.all()

    return render(request, "core/developers.html", {"all_apps": all_apps})


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


# def enable_app(request, app_id):
#     app = get_object_or_404(App, id=app_id)
#     app.enabled = True
#     app.save()

#     return redirect(reverse("developers"))


# def disable_app(request, app_id):
#     app = get_object_or_404(App, id=app_id)
#     app.enabled = False
#     app.save()

#     return redirect(reverse("developers"))

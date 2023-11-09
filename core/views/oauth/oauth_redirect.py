from authlib.integrations.django_client import OAuthError
from core.utils.recurse_api import get_user_profile
from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from .utils import get_rc_oauth


def oauth_redirect(request):
    try:
        token = get_rc_oauth().authorize_access_token(request)
    except OAuthError as exception:
        if exception.error == "access_denied":
            return HttpResponse(
                f"""looks like you denied access, that's ok. <a href="{reverse('developers')}">want to try again?</a>""".encode(
                    "utf-8"
                )
            )
        raise

    profile = get_user_profile(token["access_token"])

    User = get_user_model()
    # we are not storing the token/refresh token/expires, etc. as in
    # https://github.com/gregsadetsky/checkintopus/blob/main/core/views.py#L41
    # as we are only using the rc oauth login flow as a 'light' login layer
    # i.e. if a user can login through RC to us, we sign them in and that's good enough.
    # yes, presumably, they could remove oauth access from the app and/or not be allowed
    # to login to rc and we would not log them out / check the oauth/their profile validity
    # the worse case is that they'd still have access to this (rctv) app.
    # we don't consider this a 'security risk'.
    username = f'rc-{profile["id"]}'
    user, _ = User.objects.update_or_create(
        username=username,
        defaults={
            "username": username,
        },
    )

    login(request, user)

    # was this developer logging in while working with an app/the sdk?
    # if so, we should have their app url in the session. redirect to it
    # and clear the session value
    redirect_uri = request.session.get("redirect_uri", None)
    if redirect_uri:
        request.session["redirect_uri"] = None
        return redirect(redirect_uri)

    # 'regular' case of accessing /developers and being hit with an oauth login
    # just go to /developers then!
    return redirect(reverse("developers"))

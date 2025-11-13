from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.http import HttpResponseForbidden


def view_or_expect_tv_token(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view(request, *args, **kwargs)
        else:
            tv_login_token = request.GET.get("tv_login_token")

            if tv_login_token and tv_login_token == settings.TV_LOGIN_TOKEN:
                # find 'tv' user and log them in
                User = get_user_model()
                user = User.objects.get(username="tv")
                login(request, user)
                # need to override this I guess..?
                request.user = user
                return view(request, *args, **kwargs)

            return HttpResponseForbidden()

    return wrapper

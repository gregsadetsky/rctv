from django.http import HttpResponseForbidden

# create decorator for all /api/ views in core/urls.txt that
# checks whether user is authed, lets view through, or otherwise rejects it with a 403


def user_authentication_required(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return wrapper

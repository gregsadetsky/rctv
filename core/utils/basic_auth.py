import base64
from functools import wraps

from django.contrib.auth import authenticate
from django.http import HttpResponse


# https://gist.github.com/codeinthehole/4732233
def view_or_basicauth(view, request, *args, **kwargs):
    # Check for valid basic auth header
    print("request.META", request.META)
    if "HTTP_AUTHORIZATION" in request.META:
        auth = request.META["HTTP_AUTHORIZATION"].split()
        print("auth", auth)
        if len(auth) == 2:
            if auth[0].lower() == "basic":
                uname, passwd = base64.b64decode(auth[1]).split(b":")
                user = authenticate(
                    username=uname.decode("utf-8"),
                    password=passwd.decode("utf-8"),
                )
                if user is not None and user.is_active:
                    request.user = user
                    return view(request, *args, **kwargs)

    # Either they did not provide an authorization header or
    # something in the authorization attempt failed. Send a 401
    # back to them to ask them to authenticate.
    response = HttpResponse()
    response.status_code = 401
    response["WWW-Authenticate"] = 'Basic realm="django"'
    return response


# decorator, checks user/password using basic auth against users db
def basicauth(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        return view_or_basicauth(view_func, request, *args, **kwargs)

    return wrapper

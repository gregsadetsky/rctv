from django.http import JsonResponse


def user_is_authed(request):
    print("user_is_authed")
    print("request.user", request.user)
    print("request.user.is_authenticated", request.user.is_authenticated)
    print("request.user.is_active", request.user.is_active)
    # is user logged in (i.e. not anonymous) & active? return true/false
    user_is_authed = request.user.is_authenticated and request.user.is_active
    return JsonResponse({"user_is_authed": user_is_authed})

from django.http import JsonResponse


def user_is_authed(request):
    # is user logged in (i.e. not anonymous) & active? return true/false
    user_is_authed = request.user.is_authenticated and request.user.is_active
    return JsonResponse({"user_is_authed": user_is_authed})

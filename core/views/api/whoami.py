from django.http import JsonResponse


def whoami(request):
    # is user logged in & enabled? return true/false
    return JsonResponse({"is_authenticated": request.user.user_can_authenticate()})

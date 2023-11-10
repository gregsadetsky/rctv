from django.http import JsonResponse

from ...models import App, IncomingZulipMessage
from ...utils.views_auth import user_authentication_required


@user_authentication_required
def get_unprocessed_zulip_messages(_request):
    unprocessed_zulip_messages = IncomingZulipMessage.objects.filter(
        processed=False
    ).order_by("created_at")

    # make a copy of the payloads, otherwise the .filter and
    # the .update below will ""clash"" and
    # unprocessed_zulip_messages will end up containing an empty list...!!
    payloads = [m.payload for m in unprocessed_zulip_messages]

    # mark them all as processed
    unprocessed_zulip_messages.update(processed=True)

    return JsonResponse({"unprocessed_zulip_messages": list(payloads)})

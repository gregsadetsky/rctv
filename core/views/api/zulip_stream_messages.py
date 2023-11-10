from django.http import JsonResponse

from ...utils.zulip_api import get_last_ten_messages_from_stream


def zulip_stream_messages(request):
    # get stream name
    stream_name = request.GET.get("stream", None)
    assert stream_name is not None
    # optional - filter by sender
    sender = request.GET.get("sender", None)

    found_messages = get_last_ten_messages_from_stream(
        stream_name=stream_name, sender=sender
    )
    return JsonResponse({"messages": found_messages})

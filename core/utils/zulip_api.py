from pathlib import Path

import zulip
from django.conf import settings

APPROVED_STREAMS = ["RCTV", "blogging", "random", "cute"]

# config values will be fetched from the ZULIP_* environment variables
client = zulip.Client()


# zulip api at large:
# https://zulip.com/api/
# api doc re: creating a 'narrow' i.e. searching
# https://zulip.com/api/construct-narrow
def get_last_ten_messages_from_stream(stream_name, sender=None):
    assert stream_name in APPROVED_STREAMS
    request_narrow_payload = [
        {"operator": "stream", "operand": stream_name},
    ]

    if sender:
        request_narrow_payload.append({"operator": "sender", "operand": sender})

    request = {
        "anchor": "newest",
        "num_before": 10,
        "num_after": 0,
        "narrow": request_narrow_payload,
    }
    return client.get_messages(request)

from pathlib import Path

import zulip

ZULIP_RC = Path(__file__).resolve().parent.parent / ".zuliprc"
assert ZULIP_RC.exists()

client = zulip.Client(config_file=ZULIP_RC)

# TODO WIP WIP WIP - gets latest message from #RCTV stream
# do more/other things
# i.e. let frontend fetch some? any? messages from some/any stream?

# zulip api at large:
# https://zulip.com/api/
# api doc re: creating a 'narrow' i.e. searching
# https://zulip.com/api/construct-narrow

request = {
    "anchor": "newest",
    "num_before": 1,
    "num_after": 0,
    "narrow": [{"operator": "stream", "operand": "RCTV"}],
}
result = client.get_messages(request)
print(result)

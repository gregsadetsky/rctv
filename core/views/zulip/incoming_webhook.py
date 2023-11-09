import json
import random
import re

from django.conf import settings
from django.core.validators import URLValidator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ...models import ZulipImgRequest
from .agreements import AGREEMENTS

BOT_NAME = settings.ZULIP_INCOMING_WEBHOOK_BOT_NAME


@csrf_exempt
def incoming_webhook(request):
    message_data = json.loads(request.body)

    assert len(message_data["token"]) and len(settings.ZULIP_INCOMING_WEBHOOK_TOKEN)
    assert message_data["token"] == settings.ZULIP_INCOMING_WEBHOOK_TOKEN

    res = re.search(rf"^@\*\*{BOT_NAME}\*\* /img (.+)$", message_data["data"])
    if not res:
        return JsonResponse(
            {
                "content": f"""I don't understand that. My commands right now are:
**@{BOT_NAME} /img SOMEURL**
""".strip()
            }
        )
    img_url = res.group(1)

    validator = URLValidator()
    try:
        validator(img_url)
    except Exception:
        return JsonResponse({"content": "That doesn't look like a valid URL."})

    ZulipImgRequest.objects.create(img_url=img_url)

    return JsonResponse({"content": random.choice(AGREEMENTS)})

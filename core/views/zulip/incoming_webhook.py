import json
import random
import re

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ...models import IncomingZulipMessage
from .agreements import AGREEMENTS

BOT_NAME = settings.ZULIP_INCOMING_WEBHOOK_BOT_NAME


@csrf_exempt
def incoming_webhook(request):
    message_data = json.loads(request.body)

    assert len(message_data["token"]) and len(settings.ZULIP_INCOMING_WEBHOOK_TOKEN)
    assert message_data["token"] == settings.ZULIP_INCOMING_WEBHOOK_TOKEN

    del message_data["token"]

    IncomingZulipMessage.objects.create(payload=message_data)

    return JsonResponse({"content": random.choice(AGREEMENTS)})

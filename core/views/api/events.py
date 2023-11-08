from datetime import datetime, timedelta

import recurring_ical_events
from django.conf import settings
from django.core.exceptions import BadRequest
from django.http import JsonResponse

from ...utils.calendar_api import get_events

API_TIME_FORMAT = "%Y%m%d"


def events(request):
    # optional start query param
    start = request.GET.get("start", None)
    # optional end query param
    end = request.GET.get("end", None)

    """
    Takes an optional query paramters ?start=YYYYMMDD and &end=YYYYMMDD
    Returns calendar events as JSON between [start, end] date ranges
    """

    # This either returns the cached calendar or makes an API call
    # This isn't ideal because if some RCTV is not regularly hitting this API we
    # are going to get cache-misses and do the full API request which comes out
    # to be 1.2 MB
    #
    # An alternative approach is to use something like fastapi_utils.repeat_every
    # to run this on a periodic basis instead:
    #
    # https://fastapi-utils.davidmontague.xyz/user-guide/repeated-tasks/
    cal = get_events(settings.RC_CALENDAR_URL)

    try:
        start_datetime = (
            datetime.strptime(start, API_TIME_FORMAT)
            if start is not None
            else datetime.now()
        )
        end_datetime = (
            datetime.strptime(end, API_TIME_FORMAT)
            if end is not None
            else start_datetime + timedelta(days=(2 * 365))
        )
    except ValueError:
        raise BadRequest(
            "'start' and 'end' params must be formatted in %Y%m%d. Example: 20250101"
        )

    events = recurring_ical_events.of(cal)
    events = events.between(
        start_datetime.strftime(API_TIME_FORMAT), end_datetime.strftime(API_TIME_FORMAT)
    )
    j = []
    for event in events:
        if "SUMMARY" in event:
            if "STATUS" in event and event["STATUS"] == "CANCELLED":
                continue
            e = {}
            e["summary"] = event["SUMMARY"]
            e["start"] = event["DTSTART"].dt
            e["end"] = event["DTEND"].dt
            duration = event["DTEND"].dt - event["DTSTART"].dt
            e["duration_seconds"] = duration
            e["duration_string"] = str(duration)
            e["description"] = event["DESCRIPTION"]
            e["location"] = event.get("LOCATION", None)
            j.append(e)

    return JsonResponse({"events": j})

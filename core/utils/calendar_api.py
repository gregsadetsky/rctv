from functools import lru_cache
import time
import requests
import icalendar
import recurring_ical_events

CACHE_DURATION = 15 * 60  # 15 minutes


class CalendarFetchError(Exception):
    pass


def get_events(url):
    return _load_events(url, ttl_hash=is_time())


# Determines if we should refresh the
def is_time(seconds=CACHE_DURATION):
    """
    Returns the same number until CACHE_DURATION has elapsed.

    E.g.
    CACHE_DURATION = 5 minutes
    is_time() -> 56645190
    sleep(10 minutes)
    is_time() -> 56646193

    @lru_cache is going to notice the arguments change and therefore re-run the
    function
    """
    return round(time.time() / seconds)


@lru_cache(maxsize=1, typed=True)
def _load_events(url, ttl_hash=None):
    """
    Fetches Calendar Events from a Recruse Calendar subscription URL

    Returns an icalendar Calendar objectt

    LRU Cache depends on the unique arguments to the function
    After CACHE_DURATION has elapsed, ttl_hash will be different value which
    tells @lru_cache to re-run this function and cache its result
    """
    #  TTL is not used directly, instead its purpose is as type information to @lru_cache
    del ttl_hash

    r = requests.get(url)

    if not r.ok:
        raise CalendarFetchError

    assert r.ok, f"Calendar Request Failed: {r}"

    ics = r.text
    calendar = icalendar.Calendar.from_ical(ics)
    return calendar

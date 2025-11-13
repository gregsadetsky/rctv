"""
WSGI config for rctv project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

if "DJANGO_SETTINGS_MODULE" not in os.environ:
    import sys, time
    print("ERROR: you must set DJANGO_SETTINGS_MODULE=rctv.settings.dev (or other) before running the server", file=sys.stderr)
    print("ERROR: (Ctrl+C to exit and solve this problem.)", file=sys.stderr)
    while True:
        time.sleep(999)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

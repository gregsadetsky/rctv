#!/usr/bin/env bash

reload_args="--reload"
# The --reload option automatically watches for code changes.
# We must enumerate other files that we want to trigger a reload.
for f in \
    core/templates/core/*.html \
    core/static/core/*.jpg \
; do
    reload_args="$reload_args --reload-extra-file $f"
done

DJANGO_SETTINGS_MODULE=rctv.settings.dev exec gunicorn $reload_args rctv.wsgi

#!/usr/bin/env bash

# The --reload-include options require the watchfiles module be installed.
exec dotenv run uvicorn --reload \
    --reload-include '*.html' \
    --reload-include '*.jpg' \
    rctv.asgi:application

#!/usr/bin/env bash

exec uvicorn --host 0.0.0.0 --port 8000 rctv.asgi:application

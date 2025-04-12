#!/usr/bin/env bash
# exit on error
set -o errexit

gunicorn --access-logformat '%(h)s %(l)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" reqtime: %(M)s ms' rctv.wsgi:application

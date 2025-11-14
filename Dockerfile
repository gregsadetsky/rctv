FROM python:3.12-slim

WORKDIR /code

# docker will not re-pip install if requirements.txt doesn't change
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code

# Build the django static files.
# Note: the .env secret contains a few newline-separated NAME='value' overrides for deployment.
# In dev, the .env secret is empty. (It has nothing to do with the .env file in the cwd, which is also used.)
RUN --mount=type=secret,id=.env env $(cat /run/secrets/.env | xargs) python manage.py collectstatic --no-input

# launch it
CMD ["bin/serve.sh"]

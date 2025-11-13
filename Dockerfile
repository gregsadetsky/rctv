FROM python:3.12-slim

WORKDIR /code

# docker will not re-pip install if requirements.txt doesn't change
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code

# build the django static files
RUN --mount=type=secret,id=.env env $(cat /run/secrets/.env | xargs) python manage.py collectstatic --no-input

# launch it
CMD ["bin/serve.sh"]

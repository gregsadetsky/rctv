FROM nikolaik/python-nodejs:python3.12-nodejs22

WORKDIR /code

# docker will not re-pip install if requirements.txt doesn't change
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY ./sdk/package.json /code/sdk/package.json
COPY ./sdk/bun.lockb /code/sdk/bun.lockb
RUN (cd sdk && npm install bun && bun install && bun bundle)

# building the vite project implies more files - package lock,
# tsconfig (which we're not using, but could),
# the main typescript and all related typescript code.... so just include everything
# at this point
COPY . /code
RUN (cd /code/core/static_src && npm install && npm run build)

# build the django static files, passing the env vars to the command
# otherwise the django build will fail
RUN --mount=type=secret,id=.env env $(cat /run/secrets/.env | xargs) python manage.py collectstatic --no-input

# launch it
CMD ["bin/serve.sh"]

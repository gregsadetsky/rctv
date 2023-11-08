# RCTV

## Development basics

### You need a PostgreSQL database

For the project to work in development mode, you'll need to have PostgreSQL running, and PostgreSQL will need to have a database named `rctv` inside it. If you're on mac, I suggest [Postgres.app](https://postgresapp.com/) to run postgres locally and [Postico](https://eggerapps.at/postico2/) to view & change stuff in the database.

### Getting started the first time

To get started, navigate to the directory where this code lives. If you're downloading this code fresh, you'll need to run these commands:

```
python3 -m venv venv
pip install -r requirements.txt
```

### Getting started every time

If you've done that before, or if you just did the [minimalish-django-starter setup](https://github.com/gregsadetsky/minimalish-django-starter), you can skip those two lines and just run

```
source venv/bin/activate
python manage.py runserver
```

If you get hollered at to run some other command like `python manage.py migrate` hit Ctrl-C to stop the server, do that and then run `python manage.py runserver` again, no worries.

-----

[powered by minimalish django starter](https://github.com/gregsadetsky/minimalish-django-starter) 

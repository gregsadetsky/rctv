# RCTV

## what is this

an IRL tv dashboard at the [Recurse Center](https://recurse.com/) with "tv apps" to bridge the physical-virtual schism

## how to dev (backend)

- you need a local postgres db
- copy .env.example to .env and fill it out

first time:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

also! create a django super user for yourself!

```bash
python manage.py createsuperuser
# answer admin (username), a@a.ca, admin (password) and 'y' to confirm the bad password
```

every time:
```bash
source venv/bin/activate
python manage.py runserver
```

## how to dev (sdk/js) - short version

- make sure that bun is installed, see sdk/README.md for more details

from repo dir:
```bash
cd sdk
bun watch
```

## raspi things

- [raspberry pi files repo is here](https://github.com/gregsadetsky/rctv-raspi).

## deployment

https://rctv.recurse.com

- hosted on greg's render account
- site is automatically deployed upon git pushing to this repo

### TODO/docs

- see [TODO](./docs/TODO.md)
- and [HOWTODEV-OAUTH](./docs/HOWTODEV-OAUTH.md)

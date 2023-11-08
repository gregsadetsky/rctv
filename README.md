# RCTV

## how to dev (backend)

- you need a postgres db
- copy .env.example to .env and fill it out

first time:
```bash
python3 -m venv venv
pip install -r requirements.txt
```

also! create a django super user for yourself!

```bash
python manage.py createsuperuser
# answer admin, a@a.ca, admin (password) and 'y' to confirm the bad password
```

every time:
```bash
source venv/bin/activate
python manage.py runserver
```

## how to dev (sdk/js) - short version

from repo dir:
- `cd sdk`
- (see instructions in README.md there for installation, etc.)
- `bun watch`

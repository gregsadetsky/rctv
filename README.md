# RCTV

## what is this

an IRL tv dashboard at the [Recurse Center](https://recurse.com/) with "tv apps" to bridge the physical-virtual schism

## how to dev (backend)

- you need a local postgres db

### first time:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

duplicate `.env.example` and name the copy `.env` and fill in the values inside `""` quotes:

```bash
cp .env.example .env
```

Initialize the database and create a django super user for yourself!

```bash
python manage.py migrate
python manage.py createsuperuser
# answer admin (username), a@a.ca, admin (password) and 'y' to confirm the bad password
```

(optional) create the `tv` user to enable TV login token auth method.
http://127.0.0.1:8000/admin/core/user/add/ (login as the superuser).
Username: `tv`, Password: (generate something secure; it will never be used).
This enables passing `?tv_login_token=<TV_LOGIN_TOKEN from .env>` to some APIs, e.g. `/get_all_apps_for_tauri`.

### every time:

```bash
source venv/bin/activate
./bin/dev.sh
```

Login as the superuser you created to bypass the oauth stack while developing locally: http://127.0.0.1:8000/admin/login/

## raspi things

- the most up to date (as of August 2025) app that runs on the pi [is here](https://github.com/gregsadetsky/rctv-tauri)!!! rust baby!!!
- previous [raspberry pi files repo is here](https://github.com/gregsadetsky/rctv-raspi).

## deployment

https://rctv.recurse.com

- hosted on the recurse disco pi!
- site is automatically deployed upon git pushing to this repo

### TODO/docs

- see [TODO](./docs/TODO.md)
- and [HOWTODEV-OAUTH](./docs/HOWTODEV-OAUTH.md)
- while you're here, read a little bit about the development process for RCTV [here](./docs/Screen%20Shot%202023-11-10%20at%206.06.17%20PM.png).

## THANKS

- Jacob Young for creating this with Greg!
- all of the RCTV app creators!!
- the Recurse Center for making it happen!!! y'all are the real deal!!
- Frank Chiarulli for his collab in bringing up the tauri client on the new pi!
- Sharon Sung for her work in making the couches zoom integration perfect!
- Josh Wolfe for being the wielder of a laser scalpel and perfectly getting rid of a metric ton of legacy code!

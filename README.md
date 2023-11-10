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

## how to dev (sdk / frontend app javascript) - short version

1. make sure that bun is installed, see sdk/README.md for more details

from repo dir:
```bash
cd sdk
bun watch
```

2. you will also need to run the vite bundler in parallel for app.html frontend scripts

first time:
```bash
cd core/static_src
npm install
```

then every time - from repo dir:
```bash
cd core/static_src
npm run dev
```

3. we're not done...

- you'll want to run `ngrok` and go [through these steps](docs/HOWTODEV-OAUTH).md so that rctv-dev.recurse.com works & points to your local django localhost:8000
- we might have even more terminals/servers to run simultaneously (when we introduce websockets??), stay tuned.........

## raspi things

- [raspberry pi files repo is here](https://github.com/gregsadetsky/rctv-raspi).

## deployment

https://rctv.recurse.com

- hosted on greg's render account
- site is automatically deployed upon git pushing to this repo

### TODO/docs

- see [TODO](./docs/TODO.md)
- and [HOWTODEV-OAUTH](./docs/HOWTODEV-OAUTH.md)
- while you're here, read a little bit about the development process for RCTV [here](./docs/Screen%20Shot%202023-11-10%20at%206.06.17%20PM.png).

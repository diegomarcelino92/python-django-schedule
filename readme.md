# Getting Started

## Requirements

- Docker
- Python3

## Install dependencies

```sh
pip install -r requirements.txt
```

## Database

### Up database

```sh
docker-compose up -d
```

### Activate venv

```sh
. venv/bin/activate 
```

### Run migration

```sh
python manage.py migrate
```

### Run seeds

```sh
python manage.py loaddata */fixtures/*.json
```

## Server

### Run

```sh
python manage.py runserver
```

### Default user

```
username: development
password: 123123
```

## Admin

### Create super user and fill password

```sh
    python manage.py createsuperuser --email admin@email.com --username admin
```

PS: You can access /admin with username `admin` and filled password

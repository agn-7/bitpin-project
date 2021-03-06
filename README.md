[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/)
[![CI](https://github.com/agn-7/bitpin-project/workflows/build/badge.svg)](https://github.com/agn-7/bitpin-project/actions/workflows/github-actions.yml)
[![codecov](https://codecov.io/gh/agn-7/bitpin-project/branch/main/graph/badge.svg?style=flat-square)](https://codecov.io/gh/agn-7/bitpin-project) 
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) 

# bitpin-project

## Django + Docker + Postgresql + DRF + pytest

### Running

Normally you can run the project in development mode:

```bash
cd bitpin
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

The project can also be run in production mode:

```bash
docker-compose up -d --build
docker exec -it bitpin_app python manage.py createsuperuser --settings=bitpin.product_settings
```

Then it's time to go to the `/admin` and create some content instances. Next, check them all and/or rate them using the following endpoints:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/v1/content/` | GET | READ | Get all contents
`api/v1/rate/:content_id/` | POST | CREATE | Create a new vote
`api/v1/rate/`| POST | CREATE | Create a new vote
`api-token-auth/` | POST | READ | Get a token

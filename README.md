[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/)
[![CI](https://github.com/agn-7/bitpin-project/workflows/build/badge.svg)](https://github.com/agn-7/bitpin-project/actions/workflows/github-actions.yml)
[![codecov](https://codecov.io/gh/agn-7/bitpin-project/branch/main/graph/badge.svg?style=flat-square)](https://codecov.io/gh/agn-7/bitpin-project)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)

# bitpin-project

## Django + Docker + Postgresql + DRF + pytest + Kubernetes

### Running

Normally you can run the project in development mode:

```bash
cd bitpin
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

The project can also be run in production mode using docker compose:

```bash
docker-compose up -d --build
docker exec -it bitpin_app python manage.py createsuperuser --settings=bitpin.production_settings
```

Or via Kubernetes (microk8s):

```bash
docker compose build
docker run -d -p 5000:5000 --restart=unless-stopped --name registry registry:2
docker tag bitpin:1.0.0 localhost:5000/bitpin:1.0.0
docker tag nginx:alpine localhost:5000/nginx:alpine
docker push localhost:5000/bitpin:1.0.0
docker push localhost:5000/nginx:alpine

mkdir manifests
find k8s/ -name "*.yml" | xargs -I{} cp {} manifests/
microk8s enable dns storage
microk8s kubectl apply -f manifests
microk8s kubectl get all

microk8s kubectl get pods --show-labels
microk8s kubectl label pods bitpin-nginx app=bitpin-nginx
microk8s kubectl exec -it <bitpin-app-pod-name> bash
python manage.py createsuperuser --settings=bitpin.production_settings

microk8s kubectl port-forward service/bitpin-nginx-service 8080:80
```


Then it's time to go to the `/admin` and create some content instances. Next, check them all and/or rate them using the following endpoints:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/v1/content/` | GET | READ | Get all contents
`api/v1/rate/:content_id/` | POST | CREATE | Create a new vote
`api/v1/rate/`| POST | CREATE | Create a new vote
`api-token-auth/` | POST | READ | Get a token

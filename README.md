# Search Engine Web Application with Django and Elasticsearch

![screenshot](screenshot.png)

## Elasticsearch and Kibana Setup (Windows)

### Dcoker and Docker-compose required

```docker
$ cd docker
$ docker-compose up -d
```

<!-- Elasticsearch:

```docker
$ docker run -d --name es01 --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "ES_JAVA_OPTS=-Xms512m -Xmx512m" docker.elastic.co/elasticsearch/elasticsearch:7.15.1
```

Kibana:

```docker
$ docker run -d --name kib01 --net elastic -p 5601:5601 -e "ELASTICSEARCH_HOSTS=http://es01:9200" docker.elastic.co/kibana/kibana:7.15.1
``` -->

Navigate:

* Elasticsearch at `http://localhost:9200`
* Kibana at `http://localhost:5601`

---

## Project Setup (Windows)

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ .\env\Scripts\activate
(env)$ 
```

Then install the dependencies:

```sh
(env) pip install -r requirements.txt
```

<!-- ## Environment

Setup your environment follow this:

```env

``` -->

## Run and compile Django

```sh
(env)$ python manage.py runservr
```

And navigate to `http://127.0.0.1:8000/`

---

## Reference

* [Docker](https://www.docker.com/)
* [Elasticsearch](https://www.elastic.co/)
* [Kibana](https://www.elastic.co/kibana/)
* [Django](https://www.djangoproject.com/)
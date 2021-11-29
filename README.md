# Search Engine Web Application with Django and Elasticsearch

![screenshot](screenshot.png)

## Elasticsearch and Kibana Setup (Windows)

### Dcoker and Docker-compose required with `docker-compose.yaml`

```docker
$ cd docker
$ docker-compose up -d
```

Navigate:

* Elasticsearch at `http://localhost:9200`
* Kibana at `http://localhost:5601`

### Create Index with thai analyzer in `kibana dev tools`

```json
PUT /covid
{
  "settings": {
    "index": {
      "number_of_shards": "3",
      "number_of_replicas": "1",
      "analysis": {
        "analyzer": {
          "thai": {
            "filter": [
              "lowercase"
            ],
            "tokenizer": "thai"
          }
        }
      }
    }
  },  
  "mappings": {
    "properties": {
      "topic": {
        "type": "text",
        "analyzer": "thai"
      },
      "content": {
        "type": "text",
        "analyzer": "thai"
      }
    }
  }
}
```

### Insert data to elasticsearch with `covid.ndjson` file

```sh
curl localhost:9200/covid2/_bulk -H "content-type:application/x-ndjson" --data-binary "@covid.ndjson"
```

### Check data in elasticsearch

```sh
GET /covid/_search
```

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
* [ndjson](http://ndjson.org/)
* [Django](https://www.djangoproject.com/)
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Covid

@registry.register_document
class CovidDocument(Document):
  class Index:
    name = 'covid'
    settings = {
      "number_of_shards" : "3",
      "number_of_replicas" : "1",
    }
  
  class Django:
    model = Covid
    fields = [
      'topic',
      'content'
    ]
  
from django.db import models

class Covid(models.Model):
  topic = models.CharField(max_length=50)
  content = models.TextField()
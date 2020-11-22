from django.db import models
from django.conf import settings
from datetime import datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    publication_date = models.DateTimeField(default=datetime.now())
    updated_date = models.DateTimeField(null=True)
    deleted_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

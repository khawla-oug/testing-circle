from django.db import models

# Create your models here.


from django.db import models
from django.utils import timezone


# article model

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

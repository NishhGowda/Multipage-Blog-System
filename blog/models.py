
# Create your models here.
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField() # Enter manually (e.g., "2025-02-23 14:30:00")

    def __str__(self):
        return self.title

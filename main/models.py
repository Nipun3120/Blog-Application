from django.db import models
from django.contrib.auth.models import User



class BlogTitle(models.Model):
    title = models.CharField(max_length = 64)

    def __str__(self):
        return self.title

class Blog(models.Model):
    author = models.CharField(max_length = 64, default = False)        
    title = models.OneToOneField(BlogTitle, on_delete=models.CASCADE)
    category = models.CharField(max_length = 64)
    content = models.TextField()

    def __str__(self):
        return self.author
        
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(unique = True,max_length = 200)
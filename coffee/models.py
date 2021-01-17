from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Cafea(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField()
    tip = models.CharField(max_length= 20)
    image = models.FilePathField(path="/img")
    
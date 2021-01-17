from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Cafea(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField()
    tip = models.CharField(max_length= 20)
    image = models.FilePathField(path="/img")

class Comment(models.Model):
    text = models.CharField(max_length=200)
    cafea = models.ForeignKey(Cafea, on_delete=models.CASCADE, related_name="comments")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
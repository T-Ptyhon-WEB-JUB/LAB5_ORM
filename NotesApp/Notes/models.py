from pydoc import describe
from django.db import models

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=2048)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=2048)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
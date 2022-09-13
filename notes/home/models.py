from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=2024)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

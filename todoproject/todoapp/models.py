from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.title
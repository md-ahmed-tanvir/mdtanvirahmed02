from django.db import models

class Contract(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    desc = models.TextField()